any instead of interface{}

generic when possible instead of any


a := &struct{}  instead of new(struct)
a := struct{}


??
if err := sth ; err != nil {
}
This is useful when you don't need the err variable later and prefer to keep its scope as narrow as possible.

even defining vasr in for loop with s := sth instead of var s foo, and then using it in loop

default a:= , rare cases which explict needs var a sth = this, and rare only var a sth (not initial value, better than a:=0 (which is a magical number))


TODO: golang-ci read rule.
- magic number
- magic strings


use of inline function to output things to functions which they do not recieve (they should accept `func` types though)

binary search:
//slice.binarySearch??
func binarySearch(sortedSlice []int, target int) int {
    index := sort.Search(len(sortedSlice), func(i int) bool {
        return sortedSlice[i] >= target
    })
    if index < len(sortedSlice) && sortedSlice[index] == target {
        return index // Found
    }
    return -1 // Not found
}

see, though sort.Search doesn't receive any slice, it can be used as inline function, to input it our sortedSlice !!!!!
