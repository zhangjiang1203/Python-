import os
import re
import xlwt
import xlrd
from xlutils.copy import copy

resultSheet = "analyzeResult"
# 去除文本中的 [-Wdeprecated-declarations] 的标识
subPattern = "\[(.*)\]"

log_file_name = "Analyze DYHeart_2024-02-04T15-47-10.txt"
excel_file_name = "analyze_result2.xls"

# 错误提示展示数据
callAndMessage = "core.CallAndMessage"  # .    logicError
retainCycles = "Warc-retain-cycles"  # ,  代码中可能存在一个保留环，可能导致内存泄露。
unreachableCode = "Wunreachable-code"  # ,  代码因为程序逻辑而永远不会被执行
uninitialized = "Wsometimes-uninitialized"  # , 代码中存在一些变量在某些执行路径下可能未初始化就被使用了
performSelectorLeaks = "Warc-performSelector-leaks"  # , 使用 performSelector: 可能导致内存泄露的情况
incompatiblePointerTypes = "Wincompatible-pointer-types"  # 指出了一个指针赋值或函数参数传递时存在类型不兼容的问题。这意味着你试图将一种类型的指针赋值给另一种类型的指针
objCProperty = "osx.ObjCProperty"  # 属性修饰问题，结合上下文
missingSuperCall = "osx.cocoa.MissingSuperCall"
missingSuperCalls = "-Wobjc-missing-super-calls"  # 子类中的对应方法中未正确调用父类的实现
incompleteImplementation = "Wincomplete-implementation"  # 类中声明方法，但并没有在文件中实现
deadCode = "deadcode.DeadStores"  # 定义未使用变量
unusedVariable = "Wunused-variable"  # . 变量被声明但未被使用
declarations = "Wdeprecated-declarations"  # 方法过期
protocol = "Wprotocol"  # 未遵守协议
attributeMismatch = "Wproperty-attribute-mismatch"  # 属性声明的特性与其实际的使用方式不匹配
missingDeclarations = "Wmissing-declarations"  # 在当前文件中找不到某些函数或变量的声明
deprecatedImplementations = "Wdeprecated-implementations"  # 使用已被标记为过时的接口或方法时发出警告
nilArg = "osx.cocoa.NilArg"  # NilArg可能指代对这样的空对象进行操作或传递给函数和方法作为参数
unusedConstVariable = "Wunused-const-variable"  # , 有常量变量未被引用
extraArgs = "Wformat-extra-args"  # printf 类型的函数提供了多余的参数时发出警告

workdir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(workdir, excel_file_name)
# 过滤的组件名
ignore_module = ["Headers", "ld", "Sentry", "FlipperKit", "QCloudCore", "Flipper-PeerTalk", "React-Core",
                 "DYSentryServiceKit", "AliyunLogProducer", "DYPhotoPicker",
                 "libwebp", "DYSPerformanceMonitor", "DYDebugToolKit", "DYAudioComponentMediatorAPIs", "YYModel",
                 "DYLint", "DYStorage", "DYPhotoBrowser",
                 "SDWebImageWebPCoder", "DYHKRN", "DYBAudioReactNative", "React-RCTImage", "React-RCTAnimation",
                 "QCloudCOSXML", "FMDB", "LookinServer", "DYBFlipperPlugin",
                 "ld:", "YYText", "React-RCTNetwork", "DouyuBatman", "libpng", "React-RCTBlob", "SudMGPWrapper",
                 "React-RCTText", "React-CoreModules", "RNReanimated", "RNScreens",
                 "SocketRocket", "MMKVCore", "Reachability", "DYFPerformanceMonitor", "DYVap", "DYHeartVoipKit"]


def analyze_log():
    with open(log_file_name, "r", encoding='utf-8') as f:
        # 查找四类错误
        # 未使用变量错误
        deadStoreError = []
        # 逻辑错误
        logicError = []
        # 属性修饰错误
        performSelectorLeaksError = []
        # 有引用环的警告提示
        retainCyclesError = []
        # 逻辑上不可能执行的警告
        unreachableError = []
        # 未初始化使用警告
        uninitializedError = []
        # 没有调用super
        missingSuperCallError = []
        # 属性修饰问题
        propertyDecorateError = []
        # 参数多余
        extraArgsError = []
        # 过期方法
        declarationsError = []

        for line in f:
            if " warning: " in line:
                # 对数据进行解析
                subStr = line.split(" warning: ")
                # #取最后一个值进行操作
                specNameStr = subStr[0].split("Pods/")[-1]
                nameList = specNameStr.split("/")
                # 获取对应类库信息
                moduleName = nameList[0]
                # 获取文件名
                fileName = nameList[-1]
                # 获取错误信息
                errorStr = subStr[-1]
                if (moduleName not in ignore_module) & ("DYTarget" not in fileName):

                    if callAndMessage in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        logicError.append([moduleName, fileName, errorStr, "1", "", "逻辑有错误 重点关注"])

                    if retainCycles in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        retainCyclesError.append(
                            [moduleName, fileName, errorStr, "2", "", "代码中可能存在一个保留环，可能导致内存泄露"])

                    if unreachableCode in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        unreachableError.append(
                            [moduleName, fileName, errorStr, "3", "", "代码因为程序逻辑而永远不会被执行"])

                    if uninitialized in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        uninitializedError.append([moduleName, fileName, errorStr, "4", "",
                                                   "代码中存在一些变量在某些执行路径下可能未初始化就被使用了"])

                    if performSelectorLeaks in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        performSelectorLeaksError.append(
                            [moduleName, fileName, errorStr, "5", "", "使用 performSelector: 可能导致内存泄露的情况"])

                    if objCProperty in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        propertyDecorateError.append(
                            [moduleName, fileName, errorStr, "6", "", "属性修饰问题，结合上下文"])

                    if missingSuperCall in errorStr or missingSuperCalls in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        missingSuperCallError.append(
                            [moduleName, fileName, errorStr, "7", "", "子类中的对应方法中未正确调用父类的实现"])

                    if deadCode in errorStr or unusedVariable in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        deadStoreError.append([moduleName, fileName, errorStr, "8", "", "定义未使用变量"])

                    if extraArgs in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        extraArgsError.append(
                            [moduleName, fileName, errorStr, "9", "", "函数提供了多余的参数时发出警告"])

                    if declarations in errorStr:
                        errorStr = re.sub(subPattern, "", errorStr)
                        declarationsError.append(
                            [moduleName, fileName, errorStr, "10", "", "使用已被标记为过时的接口或方法"])

        write_excel_xlsx_append(file_path, resultSheet, logicError)
        write_excel_xlsx_append(file_path, resultSheet, retainCyclesError)
        write_excel_xlsx_append(file_path, resultSheet, unreachableError)
        write_excel_xlsx_append(file_path, resultSheet, uninitializedError)
        write_excel_xlsx_append(file_path, resultSheet, performSelectorLeaksError)
        write_excel_xlsx_append(file_path, resultSheet, propertyDecorateError)
        write_excel_xlsx_append(file_path, resultSheet, missingSuperCallError)
        write_excel_xlsx_append(file_path, resultSheet, deadStoreError)
        write_excel_xlsx_append(file_path, resultSheet, extraArgsError)
        write_excel_xlsx_append(file_path, resultSheet, declarationsError)


def write_excel_xls(path, sheet_name, value):
    index = len(value)
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet(sheet_name)

    for i in range(index):
        for j in range(len(value[i])):
            sheet.write(i, j, value[i][j])

    workbook.save(path)


def write_excel_xlsx_append(path, sheet_name, value):
    index = len(value)
    workbook = xlrd.open_workbook(path)
    sheet_names = workbook.sheet_names()
    # sheetName 已经存在了 算出
    new_workbook = copy(workbook)
    if sheet_name in sheet_names:
        sheet = workbook.sheet_by_name(sheet_name)
        # 表格中已经存在的数据行数
        rows_old = sheet.nrows
        sheet_index = sheet_names.index(sheet_name)
    else:
        # 添加sheet
        new_workbook.add_sheet(sheet_name)
        rows_old = 0
        sheet_index = len(sheet_names)

    new_sheet = new_workbook.get_sheet(sheet_index)
    # 保存数据
    for i in range(index):
        for j in range(len(value[i])):
            new_sheet.write(i + rows_old, j, str(value[i][j]))

    new_workbook.save(path)


if __name__ == '__main__':
    write_excel_xls(file_path, resultSheet, [["组件名", "文件名", "问题描述", "优先级", "状态", "说明"]])

    analyze_log()
