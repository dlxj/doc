
#include "sqlite3.c"
//#include "std.c"
#include "dir.c"

#define SQOK SQLITE_OK

static const char* SQMG(sqlite3 *db) {
    return sqlite3_errmsg(db);
}

static sqlite3* sqOpen_(char *dbname, int mode, int *rc) {
    sqlite3 *db;
    *rc = sqlite3_open_v2(dbname, &db, mode, NULL);
    return db;
}

static sqlite3* sqOpen(char *dbname) {
    sqlite3 *db; int rc;
    db = sqOpen_(dbname, SQLITE_OPEN_READONLY, &rc);
    if( rc != SQOK ) DBERR("Can't open database: %s", dbname);
    DBLOG("open db '%s'", dbname);
    return db;
}

static sqlite3* sqOpenCreate(char *dbname) {
    sqlite3 *db; int rc;
    db = sqOpen_(dbname, SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE, &rc);
    if( rc != SQOK ) DBERR("Can't open database: %s", dbname);
    DBLOG("open db '%s'", dbname);
    return db;
}

bool sqIsDbExsit(char *dbname) {
    sqlite3 *db; int rc;
    //DBLOG("dbname = %s", dbname);
    db = sqOpen_(dbname, SQLITE_OPEN_READONLY, &rc);
    if (rc == SQOK) {
        sqlite3_close(db);
        return true;
    }
    return false;
}

static int sqExec(
    sqlite3 *db,                // The database on which the SQL executes
    const char *zSql,           // The SQL to be executed
    sqlite3_callback xCallback, // Invoke this callback routine
    void *pArg,                 // First argument to xCallback()
    char **pzErrMsg             // Write error messages here
){
    int rc;
    rc = sqlite3_exec(db, zSql, xCallback, 0, pzErrMsg);
    if( rc!=SQOK ){
        DBLOG("SQL error: %s\n", *pzErrMsg);
        sqlite3_free(*pzErrMsg);
        ASSERT(0);
    }
    return rc;
}

static int sqPrepare(
  sqlite3 *db,            // Database handle
  const char *zSql,       // SQL statement, UTF-8 encoded
  int nByte,              // set -1, if zSql end with null, else to set it as nbytes of the buf  // Maximum length of zSql in bytes.
  sqlite3_stmt **ppStmt,  // OUT: Statement handle
  const char **pzTail     // OUT: Pointer to unused portion of zSql
){
  int rc;
  rc = sqlite3_prepare_v2(db, zSql, -1,
                     ppStmt, NULL
  );
  if (rc != SQOK || *ppStmt == NULL) DBERR("Error in sqPrepare():  %s", sqlite3_errmsg(db));
  return rc;
}

static char* sqGet(sqlite3 *db, char *word, int *out_siz) {
    char *buf;
    int rc, idx, ncol, nbyte;
    sqlite3_stmt *pStmt;
    nbyte = 0; buf = NULL;

    rc = sqPrepare(db, "SELECT pronunciation FROM vocabulary_pronunciation WHERE vocabulary = @p1;", -1, &pStmt, NULL);
    idx = sqlite3_bind_parameter_index(pStmt, "@p1");
    sqlite3_bind_text(pStmt, idx, word, strlen(word)+1,  SQLITE_STATIC);
    rc = sqlite3_step(pStmt);
    if (rc == SQLITE_ROW) {
        ncol  = sqlite3_column_count(pStmt);  // 1nd col
        char *data = (char*)sqlite3_column_blob(pStmt, 0);
        nbyte = sqlite3_column_bytes(pStmt, 0);
        if (nbyte != 0) {
            buf = (char*)malloc(nbyte);
            memcpy(buf, data, nbyte);
            *out_siz = nbyte;
        }
    } else if (rc != SQLITE_DONE && rc != SQOK) {
       DBERR("Error: %s in %s", SQMG(db), __func__);
    }
    sqlite3_finalize(pStmt);
    return buf;
}

static bool sqIsWordExist(sqlite3 *db, char *word) {
    int siz;
    if (sqGet(db, word, &siz) != NULL && siz != 0) return true;
    return false;
}

static void sqPut(sqlite3 *db, char *word, char *buf, int siz) {
    int rc, idx;
    sqlite3_stmt *pStmt;

    if ( sqIsWordExist(db, word) ) DBERR("ERROR: word [%s] has been exist. in function %s()", word, __func__);

    rc = sqPrepare(db, "INSERT INTO vocabulary_pronunciation VALUES(@p1, @p2);", -1, &pStmt, NULL);

    idx = sqlite3_bind_parameter_index(pStmt, "@p1");
    sqlite3_bind_text(pStmt, idx, word, strlen(word)+1,  SQLITE_STATIC);

    idx = sqlite3_bind_parameter_index(pStmt, "@p2");
    sqlite3_bind_blob(pStmt, idx, buf, siz,  SQLITE_STATIC);
    sqlite3_step(pStmt);

    sqlite3_finalize(pStmt);
}

// return a NULL terminal string
static char* sqGetOrigFromInfle(sqlite3 *db, char *word, int *out_siz) {
    char *buf;
    int rc, idx, ncol, nbyte;
    sqlite3_stmt *pStmt;
    nbyte = 0; buf = NULL;

    rc = sqPrepare(db, "SELECT original_word FROM vocabulary_inflection WHERE inflection_word = @p1;", -1, &pStmt, NULL);
    idx = sqlite3_bind_parameter_index(pStmt, "@p1");
    sqlite3_bind_text(pStmt, idx, word, strlen(word)+1,  SQLITE_STATIC);
    rc = sqlite3_step(pStmt);
    if (rc == SQLITE_ROW) {
        ncol = sqlite3_column_count(pStmt);
        char *data = sqlite3_column_text(pStmt, 0);
        nbyte = sqlite3_column_bytes(pStmt, 0);  // 1nd col
        if (nbyte != 0) {
            if ( data[nbyte-1] != 0 || strlen(data) != nbyte-1) DBERR("#########ERROR: db's data not correct. in function %s()#########", __func__);
                    // strlen(data) != nbyte-1, means, it has 0 value before the end position.
            buf = (char*)malloc(nbyte);
            memcpy(buf, (void*)data, nbyte);
            *out_siz = nbyte;
        }
        // if nrow greater than 2 that was wrong. one inflection word only corresponding to one original word
        if ( sqlite3_step(pStmt) == SQLITE_ROW ) DBERR("ERROR: db not correct. please check create table and insert statement. in function %s()", __func__);
    } else if (rc != SQLITE_DONE && rc != SQOK) {
       DBERR("Error: %s in %s", SQMG(db), __func__);
    }
    sqlite3_finalize(pStmt);
    return buf;
}

static bool sqIsInfleExist(sqlite3 *db, char *word) {
    int siz;
    if ( sqGetOrigFromInfle(db, word, &siz) != NULL && siz != 0 ) return true;
    return false;
}

static void sqPutInfle(sqlite3 *db, char *infle, char *word) {
    int rc, idx;
    sqlite3_stmt *pStmt;

    if ( sqIsInfleExist(db, infle) ) DBERR("ERROR: inflection word [%s] has been exist. in function %s()", infle, __func__);

    rc = sqPrepare(db, "INSERT INTO vocabulary_inflection VALUES(@p1, @p2);", -1, &pStmt, NULL);

    // NOTICE: in sqlite3_bind_xx function
    // To be clear: the value is the number of bytes in the value, not the number of characters.
    idx = sqlite3_bind_parameter_index(pStmt, "@p1");
    sqlite3_bind_text(pStmt, idx, infle, strlen(infle)+1, SQLITE_STATIC);

    idx = sqlite3_bind_parameter_index(pStmt, "@p2");
    sqlite3_bind_text(pStmt, idx, word, strlen(word)+1, SQLITE_STATIC);
    sqlite3_step(pStmt);

    sqlite3_finalize(pStmt);
}

static void sqPutWordWav(sqlite3 *db, char *word, char *wavfname) {
    char *buf; int siz;
    buf = data(wavfname, &siz);
    if ( ! sqIsWordExist(db, word) ) sqPut(db, word, buf, siz);
    free(buf);
}

static void sqPutInfleAndWord(sqlite3 *db, char *infle, char *word) {
    if (db == NULL) DBERR("ERROR: db is NULL in function %s", __func__);
    if ( ! sqIsInfleExist(db, infle) ) sqPutInfle(db, infle, word);
}

static char* wordFormWavPath(char *path) {
    static char buf[512];
    memset(buf, 0, 512);
    char *sufix[] = {".wav", ".WAV"};
    if (path == NULL || strlen(path) <= 0) DBERR("Error: bad argument in fuction %s", __func__);
    char *p = strrchr(path, '/');
    if (p == NULL &&
        (strstr(path, sufix[0]) == NULL && strstr(path, sufix[1]) == NULL)
    ) {
        DBERR("ERROR: wav files name must have sufix 'wav' or 'WAV'. in function %s()", __func__);
    }
    if (p != NULL && (p+1) == NULL) DBERR("ERROR: wav name is empty. in function %s()", __func__);
    if (p != NULL &&
            (strstr(p+1, sufix[0]) == NULL && strstr(p+1, sufix[1]) == NULL)
        ) {
        DBERR("ERROR: wav files name must have sufix 'wav' or 'WAV'. in function %s()", __func__);
    }

    if (p == NULL) {
        if (path[0] == '.') DBERR("ERROR: bad path. in function %s()", __func__);
        memcpy(buf, path, strlen(path) - strlen(sufix[0]));
    } else {
        if ((p+1)[0] == '.') DBERR("ERROR: bad path. in function %s()", __func__);
        memcpy(buf, p+1, strlen(p+1) - strlen(sufix[0]));
    }
    return buf;
}

void sqGenDB(char *fname, char *dir_audio) {
    sqlite3 *db;
    sqlite3_stmt *pStmt;
    int rc;

    if (sqIsDbExsit(fname)) DBERR("Error: db '%s' had been exit. in sqGenDB()", fname);
    db = sqOpenCreate(fname);

    rc = sqPrepare(db, "CREATE TABLE vocabulary_pronunciation(vocabulary TEXT PRIMARY KEY ASC, pronunciation BLOB);", -1,&pStmt, NULL);
    sqlite3_step(pStmt);
    if (rc != SQOK) DBERR("%s in %s" , SQMG(db),  __func__);
    sqlite3_finalize(pStmt);

    char *path = dir_audio;
    int nfname = 0;
    unsigned int *buf = fpaths(path, &nfname);
    if (buf != NULL && nfname <= 0) DBERR("something wrong. in %s", __func__);
    if (buf != NULL) {
        int i;
        for (i = 0; i < nfname; i++) {
            char *fwav = buf[i];
            char *word = wordFormWavPath(fwav);
            DBLOG("word = %s; fwav = %s", word, fwav);
            sqPutWordWav(db, word, fwav);
            free((void*)buf[i]);
        }
    } else {
        DBLOG("'%s' there is no files.", path);
    }
    sqlite3_close(db);
}

void sqGenSpeakDB() {
    char *fname = DBWORDWAV;
    char *dir_audio = DIRAUDIO;
    if ( !sqIsDbExsit(fname) ) {
        sqGenDB(fname, dir_audio);
    }
}

// Generate a db file that contain a table, this table has a lots of Inflection Words and it's original form.
// @orig_word:
//      a string that terminal with NULL, it contains one word.
// @sizorig  :
//      nbytes of buf orig_word
// @inflection_word:
//      a string that terminal with NULL, it contains one or more word. if it's number of word greater than 1, then use charater ',' as  seperater.
// @sizinfle:
//      nbytes of buf inflection_words
// @no_more_data:
//      set this false, if you gonna insert data. only when all things had been done, set it's value true to close db.
//      if value is true will close the db and return immediately, doing nothing else.
void sqGenDBInflectionWords(char *fname,  char *inflection_word, int sizinfle, char *orig_word, int sizorig, bool no_more_data) {
    static sqlite3 *db = NULL;
    if (no_more_data && db == NULL) DBERR("ERROR: bad argument 'no_more_data'. you try to close a NULL db. in function %s()", __func__);
    if (no_more_data && db != NULL) {
        sqlite3_close(db);
        db = NULL;
        return;
    }
    if (orig_word == NULL || sizorig <= 0 || orig_word[sizorig -1] != 0 || strlen(orig_word) != sizorig - 1) DBERR("ERROR: bad argument. in fuction %s()", __func__);
    if (inflection_word == NULL || sizinfle <= 0 || inflection_word[sizinfle -1] != 0 || strlen(inflection_word) != sizinfle - 1) DBERR("ERROR: bad argument. in fuction %s()", __func__);

    sqlite3_stmt *pStmt; int rc;
    if (db == NULL) {
        if (sqIsDbExsit(fname)) DBERR("Error: db '%s' had been exit. in %s", fname, __func__);
        db = sqOpenCreate(fname);
        rc = sqPrepare(db, "CREATE TABLE vocabulary_inflection(inflection_word TEXT PRIMARY KEY ASC, original_word TEXT);", -1,&pStmt, NULL);
        sqlite3_step(pStmt);
        if (rc != SQOK) DBERR("%s in %s" , SQMG(db),  __func__);
        sqlite3_finalize(pStmt);
    }

    if (strchr(inflection_word, SPLITTER) == NULL) {
        // no splitter, just has one inflection word
        sqPutInfleAndWord(db, inflection_word, orig_word);
    } else {
        const char *buf = inflection_word;
        int siz = sizinfle;
        unsigned int *pointerArray = NULL; int szofpointerArray = 0; int nPointer = 0;
        pointerArray = split(buf, siz, SPLITTER, &szofpointerArray);
        if (pointerArray != NULL) {
            if (szofpointerArray <= 0) DBERR("ERROR: szofpointerArray not correct. in function %s()", __func__);
            nPointer = szofpointerArray / (sizeof (char*));
            char *infwd = NULL;
            int i;
            for (i = 0; i < nPointer; i++) {
                infwd = (char*)(*(pointerArray+i));
                DBLOG("infwd = '%s' oriwd = '%s'", infwd, orig_word);
                sqPutInfleAndWord(db, infwd, orig_word);
            }
            if (pointerArray != NULL) free_split_memory(pointerArray);
        } else {
            DBERR("ERROR: function split() return NULL. if we pass right argument to it, this error not should be happen. the fist argumnt = '%s'. in function %s()",
                  inflection_word, __func__);
        }
    }
}

// NULL terminal string
char* sqGetOrigWord(char *dbname, char *inflection_word) {
    int out_siz = 0;
    if ( ! sqIsDbExsit(dbname) ) DBERR("Error: db '%s' not exit. in %s", dbname, __func__);
    sqlite3 *db = sqOpen(dbname);
    return sqGetOrigFromInfle(db, inflection_word, &out_siz);
}

//int main() {
int mainsq() {
    printf(wordFormWavPath("/root/iplay/kokia2.wav"));
    return 0;
}











