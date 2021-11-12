
#include "sqlite3.c"

//double sim(const char *, const char *);

#pragma execution_character_set("utf-8")  // "string 以utf-8 编码"

#define ASSERT(value) if (!(value)) { _asm {int 3};}
void test2() {
	int rc, idx, ncol, nbyte;
	sqlite3_stmt *pStmt = NULL;
	double d;
	char *tmp;
	sqlite3 *db;

	rc = sqlite3_open_v2("xxx.db", &db, SQLITE_OPEN_READONLY, NULL);
	ASSERT(rc == SQLITE_OK);
	ASSERT(db != NULL);
	rc = sqlite3_prepare_v2(db, "select similar('严严ab','严严cd')", -1,
		&pStmt, NULL
		);
	ASSERT(rc == SQLITE_OK && pStmt != NULL); 
	rc = sqlite3_step(pStmt);
	ASSERT(rc == SQLITE_ROW);
	ncol = sqlite3_column_count(pStmt);  // number of cols
	d = sqlite3_column_double(pStmt, 0);
	printf("相似度: %f\n", d);
	nbyte = sqlite3_column_bytes(pStmt, 0);
}

int main() {
	system("chcp 65001");
	test2();
	char *z1 = "abcdefg";
	char *z2 = "a";
	//printf("相似度：%f\n", sim(z1, z2));
	getchar();
}/**/
