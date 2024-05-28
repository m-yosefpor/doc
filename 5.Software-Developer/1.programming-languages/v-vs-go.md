go issues/challenges:
1. null safety (nil pointer derefrence issue):
		https://www.reddit.com/r/golang/comments/vjhjex/what_are_your_strategies_to_prevent_nil_pointers/
		option type
		https://github.com/tcard/sgo

	workaround:
	1. Zero Values Over Pointers (big data structs??)
	2. Constructors
	3. Method Receivers: Define methods on structs instead of writing standalone functions, also handle nil at the beggining

		```go
		func (d *Details) Value() string {
		if d == nil {
				// return zero value or error
		}
		return d.value
		}
		```

	4.
2. error handling: https://github.com/golang/go/issues?q=is%3Aissue+is%3Aopen+error+handling+label%3Aerror-handling
https://seankhliao.com/blog/12020-11-23-go-error-handling-proposals/
		result type
		1. force devlopers to handle error -> ci
		2. boiler plate

		notice:
		- this proposal is not going to fully cover all kind of nitche error handlings, as for the most of those nitche cases (like two error messages, or when a function doesn't return an error, or when some action blocks need to take place and/or not return at all), I assume the current if err != nil method is superior and makes much sense in those nitche cases. That said, not many error handling is that nitche scenarios. As I reviewed top x projects of github (list here), more than 90% of error handlings are just returning an error, with other values as null (analysis done with the following tools: https://github.com/m-yosefpor/folan). The boiler plate error handling has been among top issues for developers in numerous surveys. So here lies to a philosophical question: shall we keep the "1 way to do a thing" in all cases with blood, (if so, I would argue that a:= 2 assignment is not follwoing the practice as the is the `var a int =2` for it, (or name other), as the value for such concise operations has greatly seen effective. also does a:=2 hanldes nitche cases when some one wants to declare a as unit or int16? NO, yet they can use the more generalized non-concise syntax in thoase version.)
		So the suggesion is here to have another error handling method based for such cases, that should be so concise to cover +90% of usecases, and should not be complicated and again verbose to cover the rest 10%, as it would rather casts/turns? useless compared to the current if err!=nil again.
		the proposal is to a mix of https://github.com/golang/go/issues/65579 and (the other one) ..., err , leveraging both to provide a concise way for that
		55%:
		if err != nil {
			return <zero values of return>, err
		}
		to
		data:= getData() ?

		and for x percent that use:
		25%:
		err := getData
		if err != nil {
			return ..., fmt.Errorf(")
		}
		err := getData() ? errors.Wrap(err, "failed to get data")

		almost 75% is made of those

		?%:
		if err != nil {
			return someNonNull, err
		}

		?%:
		if err != nil {
			t.Errorf("Unexpected error parsing cidrs: %v", cidrs)
		}



		?%:
		if err != nil {
			log
			return ..., err/errors.Wrap(err)
		}

		do sth then return:
		?%:
		if err != nil {
			doSth()
			return ..., err
		}

		if err != nil {

		}


		a, b, err := sth
		if err != nil {
			do
		}

		// what if function do not return error -> compile error
		// or return two errors -> ? nil, err1, err2
			// Question: which one if nil??? what if not last pararm? what if not err?
		// what if it's not the last param? -> no problem
		a, b, err := sth() ? nil, err
		a,b := try sth() # not useful (no wrapping) instead a,b := sth()? but even this not useful as no wrapping.. what about logging

		? only comes after statement, not the expression?

		a, b, err := sth ? return a, b, error.Wrap(sth)


		a, b, err := sth ? a, b, error.Wrap(sth)


		a, b, err := sth ? ..., error.Wrap(sth)

		a, b, err := sth ? error.Wrap(err)


		issues: code coverage + adding debug prints
3. enum?


not an issue, but a feature:
- not oop

features:

- Sum Types / is (?)
- if is expression (ternary like)
- match (sum types / enums / patterns)

- iterators -> comming in go (todo: compare syntax)

- Default struct field values
- Required struct fields @[required]
- [noinit] structs
- immutable fn args by deafult, and explicit mut in call/def




syntax:
---- does go support?
nums.clone()

.filter() and .map() methods

probably in slices package: slices.filter(array)


------ v+
nums := [1, 2, 3]  (veryy handy, though might violates of one way to do a thing, but consider a:= 1 vs var a int =1 as well)
for k := range 1000 vs for i in 0 .. 1000 (what about the start id?) // also in go tempalte (and helm, etc). So better keep consistent`

for i, x := range arr , for _, x := range arr  vs for i, x in arr , for x in arr
numbers := {
	'one': 1
	'two': 2
}

func vs fn (more concise, its still readible as proved in rust)
V also supports writing numbers with _ as separator (comes handy)

f1 := 123e-2 // 1.23 possible in golang??
f2 := 456e+2 // 45600

len(string) vs str.len and str.cap (theyre a trait of the strings)





----- ? personaly like
float32, float64 vs f32, f64
fmt.Println vs println
----- ?
CamelCase vs snake_case (idiom)
Captal vs pub
default mut, specify const vs default const, specify mut
fmt.String("sth %v",var) vs string interpolation: 'sth ${var}' (one way to do a thing, a clean way to do so)
error compile unused vs warning for unused, but error on -prod (different behaviors, some programs might not compile)
type folan Struct vs struct folan (all new types start with type, consistent and better for learning all are the same as defining types)
int8, int16, int64, unit8,... vs i8, i16, i64, u8, (easier read)
int arch dependent vs int always i32
global var, vs no global var (but what if a map with mutex or other)



nums = append(nums,4) vs nums << 4
nums << [5, 6, 7] # why no pythonic [1,2,3] + [5,6,7]


------ v-
strong type vs auto cast for variable assignemtn (it's mostly an error, should be explicit)
only strconv vs str.int() (one way to do a thing)
[]byte(someString) vs some_string.bytes()
-------------------- neutral
slice 1:3 vs 1..3
string "" vs ''
switch case vs match
	match is an espression???
make([]int, 30, 40)
mut a := []int{len: 10000, cap: 30000, init: 3}
--------

in java enhanced switch, switch is an expression with
switch (sth) {
case a -> 16;
case b -> 17;
}
