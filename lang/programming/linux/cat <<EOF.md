The `cat < syntax is very useful when working with multi-line text in Bash, eg. when assigning multi-line string to a shell variable, file or a pipe.

# Examples of `cat < syntax usage in Bash:

## 1. Assign multi-line string to a shell variable

```sh
$ sql=$(cat <<EOF
SELECT foo, bar FROM db
WHERE foo='baz'
EOF
)
```

*The `$sql` variable now holds the new-line characters too. You can verify with `echo -e "$sql"`.*

## 2. Pass multi-line string to a file in Bash

```sh
$ cat <<EOF > print.sh
#!/bin/bash
echo \$PWD
echo $PWD
EOF
```

*The `print.sh` file now contains:*

```sh
#!/bin/bash
echo $PWD
echo /home/user
```

## 3. Pass multi-line string to a pipe in Bash

```sh
$ cat <<EOF | grep 'b' | tee b.txt
foo
bar
baz
EOF
```

*The `b.txt` file contains `bar` and `baz` lines. The same output is printed to `stdout`.*