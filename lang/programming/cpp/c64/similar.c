
// visual studio 源文件utf-8 编码必须要有BOM 才行
// http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=%E4%B8%A5
// https://www.sqlite.org/c3ref/create_function.html
// https://github.com/schuyler/levenshtein

# define min(x, y) ((x) < (y) ? (x) : (y))
# define max(x, y) ((x) > (y) ? (x) : (y))

// 某个utf8 字符占几个字节
// c: 必须指向utf8 字符串
static int utf8len(char *c) {
	unsigned char c1 = c[0];
	int len = -1;
	if ((c1 & 0x80) == 0) {  // 0b10000000
		len = 1;
	}
	else if ((c1 & 0xF0) == 0xF0) {  // 0b11110000
		len = 4;
	}
	else if ((c1 & 0xE0) == 0xE0) {  // 0b11100000
		len = 3;
	}
	else if ((c1 & 0xC0) == 0xC0) {  // 0b11000000 
		len = 2;
	}
	else {
		return -1;
	}
	return len;
}

/*
** Assuming z points to the first byte of a UTF-8 character,
** advance z to point to the first byte of the next UTF-8 character.
*/
// 计算字符个数
// 实现参考sqlite3 的lengthFunc 函数
static int utf8strlen(char *str) {
	int len;
	const unsigned char *z = str;
	if (z == 0) {
		return -1;
	}
	len = 0;
	while (*z){
		len++;
		//SQLITE_SKIP_UTF8(z);
		if ((*(z++)) >= 0xc0) {
			while ((*z & 0xc0) == 0x80){ z++; }
		}
	}
	return len;
}

// utf8 编码规则
/*
1字节 0xxxxxxx
2字节 110xxxxx 10xxxxxx 0xC0 0x80
3字节 1110xxxx 10xxxxxx 10xxxxxx
4字节 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
5字节 111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
6字节 1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
*/
// 假定z 指向第一个utf8 字符，函数执行完以后z 指向下一个字符
static char *nextc(char *z) {
	if (z == 0) { return 0; }
	if (*z == 0) {
		return 0;
	}
	++z;
	while ((*z & 0xC0) == 0x80) { ++z; }  // 只要最高位是10 开头就继续移动指针
	return z;
}

__declspec(dllexport) char *at(char *z, int pos) {
	char *t = z;
	int i;
	for (i = 0; i < pos; i++) {
		t = nextc(t);
	}
	return t;
}

static int utf8eq(char *c1, char *c2) {
	int i;
	if (c1 == 0 || c2 == 0 || *c1 == 0 || *c2 == 0) {
		return -1;
	}
	int len1 = utf8len(c1);
	int len2 = utf8len(c2);
	if (len1 != len2) {
		return 0;
	} else {
		for (i = 0; i < len1; i++) {
			if (c1[i] != c2[i]) {
				return 0;
			}
		}
	}
	return 1;
}

static unsigned int levenshtein(const char *word1_in, const char *word2_in) {
	const char *word1 = word1_in;
	const char *word2 = word2_in;
	int len1 = utf8strlen(word1),
		len2 = utf8strlen(word2);
	unsigned int *v = calloc(len2 + 1, sizeof(unsigned int));
	unsigned int i, j, current, next, cost;

	/* strip common prefixes */
	while (len1 > 0 && len2 > 0 && utf8eq(word1, word2)) {
		word1 = nextc(word1);
		word2 = nextc(word2);
		len1--;
		len2--;
	}

	/* handle degenerate cases */
	if (!len1) return len2;
	if (!len2) return len1;

	/* initialize the column vector */
	for (j = 0; j < len2 + 1; j++)
		v[j] = j;

	for (i = 0; i < len1; i++) {
		/* set the value of the first row */
		current = i + 1;
		/* for each row in the column, compute the cost */
		for (j = 0; j < len2; j++) {
			/*
			* cost of replacement is 0 if the two chars are the same, or have
			* been transposed with the chars immediately before. otherwise 1.
			*/
			cost = !(utf8eq(at(word1,i), at(word2,j)) || (i && j &&
				utf8eq(at(word1, i - 1), at(word2, j)) && utf8eq(at(word1,i), at(word2, j - 1))));
			/* find the least cost of insertion, deletion, or replacement */
			next = min(min(v[j + 1] + 1,
				current + 1),
				v[j] + cost);
			/* stash the previous row's cost in the column vector */
			v[j] = current;
			/* make the cost of the next transition current */
			current = next;
		}
		/* keep the final cost at the bottom of the column */
		v[len2] = next;
	}
	free(v);
	return next;
}

double sim(const char *word1, const char *word2)  {
	int len1 = utf8strlen(word1);
	int len2 = utf8strlen(word2);
	int len = max(len1, len2);
	if (len == 0) {
		return -1;
	}
	int distance = levenshtein(word1, word2);
	//return distance;
	return 1 - distance / (double)len;
}


#pragma execution_character_set("utf-8")  // "string 以utf-8 编码"
int main() {
	system("chcp 65001");
	//printf ("%s", at("严严ab", 0));
	char z1[] = "严严b";
	char z2[] = "严严a";
	printf("%s", at(z1, 0));
	printf("相似度：    %f\n", sim(z1, z2));
	getchar();
}

