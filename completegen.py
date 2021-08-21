import os
import subprocess
import sys

compileCFile = "clang -Xclang -disable-O0-optnone -S -emit-llvm " + sys.argv[1] + " -o input.ll"
file = os.getcwd() + "/outputtransformed.json"
copyJSON = "cp " + file + " ../reacttool/src"

subprocess.run(["mkdir build"], cwd="llvmpass/", shell=True)
subprocess.run(["cmake .."], cwd="llvmpass/build/", shell=True)
subprocess.run(["make"],  cwd="llvmpass/", shell=True)
subprocess.run([compileCFile],  cwd="llvmpass/", shell=True)
subprocess.run(["make"], cwd="llvmpass/build/", shell=True)
subprocess.run(["opt -enable-new-pm=0 -load build/skeleton/libSkeletonPass.so -hello1 -S input.ll -o output.ll"],  cwd="llvmpass/", shell=True)
subprocess.run(["python3 transformjson.py"],  cwd="llvmpass/", shell=True)
subprocess.run([copyJSON],  cwd="llvmpass/", shell=True)
subprocess.run(["npm start"], cwd="llvmpass/../reacttool/src", shell=True)