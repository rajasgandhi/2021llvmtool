# llvm-pass-skeleton

Run:

    $ clang -Xclang -disable-O0-optnone -S -emit-llvm input.c -o input.ll
    $ opt -enable-new-pm=0 -load build/skeleton/libSkeletonPass.so -hello1 -S input.ll -o output.ll
    