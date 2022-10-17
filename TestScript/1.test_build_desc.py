# coding:utf-8

import sys, os, re, requests,json

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    branchName = os.getenv("BranchName")