(output)
fmt.Print(a)
fmt.Println(a)


-------------------------------------------
(input)

reader := bufio.NewReader(os.Stdin)
text , err = reader.ReadString('\n')
text = strings.Replace(text, "\n", "",-1)
char , _ , err = reader.ReadRune()
---
scanner := bufio.NewScanner(os.Stdin)
scanner.Scan()
text = scanner.Text()
---
var i int
var s string
fmt.Scanf("%d",&i)
fmt.Scan(&i)
fmt.Scanln(&s)
----------------------------------
