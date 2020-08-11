/****************************************************************************
** Meta object code from reading C++ file 'groupdock.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "groupdock.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'groupdock.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_GTab_t {
    QByteArrayData data[18];
    char stringdata0[171];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_GTab_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_GTab_t qt_meta_stringdata_GTab = {
    {
QT_MOC_LITERAL(0, 0, 4), // "GTab"
QT_MOC_LITERAL(1, 5, 15), // "searchRequested"
QT_MOC_LITERAL(2, 21, 0), // ""
QT_MOC_LITERAL(3, 22, 4), // "name"
QT_MOC_LITERAL(4, 27, 12), // "SearchMethod"
QT_MOC_LITERAL(5, 40, 6), // "method"
QT_MOC_LITERAL(6, 47, 12), // "webRequested"
QT_MOC_LITERAL(7, 60, 3), // "url"
QT_MOC_LITERAL(8, 64, 14), // "pasteRequested"
QT_MOC_LITERAL(9, 79, 9), // "upCurrent"
QT_MOC_LITERAL(10, 89, 11), // "downCurrent"
QT_MOC_LITERAL(11, 101, 10), // "delCurrent"
QT_MOC_LITERAL(12, 112, 6), // "delAll"
QT_MOC_LITERAL(13, 119, 11), // "viewCurrent"
QT_MOC_LITERAL(14, 131, 12), // "pasteCurrent"
QT_MOC_LITERAL(15, 144, 9), // "popupMenu"
QT_MOC_LITERAL(16, 154, 3), // "pos"
QT_MOC_LITERAL(17, 158, 12) // "resetButtons"

    },
    "GTab\0searchRequested\0\0name\0SearchMethod\0"
    "method\0webRequested\0url\0pasteRequested\0"
    "upCurrent\0downCurrent\0delCurrent\0"
    "delAll\0viewCurrent\0pasteCurrent\0"
    "popupMenu\0pos\0resetButtons"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_GTab[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    2,   69,    2, 0x06 /* Public */,
       6,    2,   74,    2, 0x06 /* Public */,
       8,    2,   79,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       9,    0,   84,    2, 0x08 /* Private */,
      10,    0,   85,    2, 0x08 /* Private */,
      11,    0,   86,    2, 0x08 /* Private */,
      12,    0,   87,    2, 0x08 /* Private */,
      13,    0,   88,    2, 0x08 /* Private */,
      14,    0,   89,    2, 0x08 /* Private */,
      15,    1,   90,    2, 0x08 /* Private */,
      17,    0,   93,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString, 0x80000000 | 4,    3,    5,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    3,    7,
    QMetaType::Void, QMetaType::QString, 0x80000000 | 4,    3,    5,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QPoint,   16,
    QMetaType::Void,

       0        // eod
};

void GTab::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<GTab *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->searchRequested((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const SearchMethod(*)>(_a[2]))); break;
        case 1: _t->webRequested((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 2: _t->pasteRequested((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const SearchMethod(*)>(_a[2]))); break;
        case 3: _t->upCurrent(); break;
        case 4: _t->downCurrent(); break;
        case 5: _t->delCurrent(); break;
        case 6: _t->delAll(); break;
        case 7: _t->viewCurrent(); break;
        case 8: _t->pasteCurrent(); break;
        case 9: _t->popupMenu((*reinterpret_cast< const QPoint(*)>(_a[1]))); break;
        case 10: _t->resetButtons(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (GTab::*)(const QString & , const SearchMethod & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GTab::searchRequested)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (GTab::*)(const QString & , const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GTab::webRequested)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (GTab::*)(const QString & , const SearchMethod & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GTab::pasteRequested)) {
                *result = 2;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject GTab::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_meta_stringdata_GTab.data,
    qt_meta_data_GTab,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *GTab::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GTab::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_GTab.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int GTab::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 11)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 11;
    }
    return _id;
}

// SIGNAL 0
void GTab::searchRequested(const QString & _t1, const SearchMethod & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void GTab::webRequested(const QString & _t1, const QString & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void GTab::pasteRequested(const QString & _t1, const SearchMethod & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}
struct qt_meta_stringdata_GroupTab_t {
    QByteArrayData data[15];
    char stringdata0[146];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_GroupTab_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_GroupTab_t qt_meta_stringdata_GroupTab = {
    {
QT_MOC_LITERAL(0, 0, 8), // "GroupTab"
QT_MOC_LITERAL(1, 9, 12), // "groupChanged"
QT_MOC_LITERAL(2, 22, 0), // ""
QT_MOC_LITERAL(3, 23, 3), // "grp"
QT_MOC_LITERAL(4, 27, 11), // "bookChanged"
QT_MOC_LITERAL(5, 39, 5), // "index"
QT_MOC_LITERAL(6, 45, 17), // "bookViewRequested"
QT_MOC_LITERAL(7, 63, 5), // "Book*"
QT_MOC_LITERAL(8, 69, 4), // "book"
QT_MOC_LITERAL(9, 74, 17), // "fontViewRequested"
QT_MOC_LITERAL(10, 92, 13), // "menuRequested"
QT_MOC_LITERAL(11, 106, 13), // "fullRequested"
QT_MOC_LITERAL(12, 120, 11), // "changeGroup"
QT_MOC_LITERAL(13, 132, 9), // "popupMenu"
QT_MOC_LITERAL(14, 142, 3) // "pos"

    },
    "GroupTab\0groupChanged\0\0grp\0bookChanged\0"
    "index\0bookViewRequested\0Book*\0book\0"
    "fontViewRequested\0menuRequested\0"
    "fullRequested\0changeGroup\0popupMenu\0"
    "pos"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_GroupTab[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       6,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   54,    2, 0x06 /* Public */,
       4,    1,   57,    2, 0x06 /* Public */,
       6,    1,   60,    2, 0x06 /* Public */,
       9,    1,   63,    2, 0x06 /* Public */,
      10,    0,   66,    2, 0x06 /* Public */,
      11,    0,   67,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      12,    1,   68,    2, 0x08 /* Private */,
      13,    1,   71,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void, QMetaType::Int,    5,
    QMetaType::Void, 0x80000000 | 7,    8,
    QMetaType::Void, 0x80000000 | 7,    8,
    QMetaType::Void,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void, QMetaType::Int,    5,
    QMetaType::Void, QMetaType::QPoint,   14,

       0        // eod
};

void GroupTab::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<GroupTab *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->groupChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->bookChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->bookViewRequested((*reinterpret_cast< Book*(*)>(_a[1]))); break;
        case 3: _t->fontViewRequested((*reinterpret_cast< Book*(*)>(_a[1]))); break;
        case 4: _t->menuRequested(); break;
        case 5: _t->fullRequested(); break;
        case 6: _t->changeGroup((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: _t->popupMenu((*reinterpret_cast< const QPoint(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (GroupTab::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupTab::groupChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (GroupTab::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupTab::bookChanged)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (GroupTab::*)(Book * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupTab::bookViewRequested)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (GroupTab::*)(Book * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupTab::fontViewRequested)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (GroupTab::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupTab::menuRequested)) {
                *result = 4;
                return;
            }
        }
        {
            using _t = void (GroupTab::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupTab::fullRequested)) {
                *result = 5;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject GroupTab::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_meta_stringdata_GroupTab.data,
    qt_meta_data_GroupTab,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *GroupTab::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GroupTab::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_GroupTab.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int GroupTab::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 8)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 8;
    }
    return _id;
}

// SIGNAL 0
void GroupTab::groupChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void GroupTab::bookChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void GroupTab::bookViewRequested(Book * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void GroupTab::fontViewRequested(Book * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}

// SIGNAL 4
void GroupTab::menuRequested()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void GroupTab::fullRequested()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}
struct qt_meta_stringdata_MarkTab_t {
    QByteArrayData data[1];
    char stringdata0[8];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_MarkTab_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_MarkTab_t qt_meta_stringdata_MarkTab = {
    {
QT_MOC_LITERAL(0, 0, 7) // "MarkTab"

    },
    "MarkTab"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_MarkTab[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

       0        // eod
};

void MarkTab::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

QT_INIT_METAOBJECT const QMetaObject MarkTab::staticMetaObject = { {
    QMetaObject::SuperData::link<GTab::staticMetaObject>(),
    qt_meta_stringdata_MarkTab.data,
    qt_meta_data_MarkTab,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *MarkTab::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *MarkTab::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_MarkTab.stringdata0))
        return static_cast<void*>(this);
    return GTab::qt_metacast(_clname);
}

int MarkTab::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = GTab::qt_metacall(_c, _id, _a);
    return _id;
}
struct qt_meta_stringdata_HistoryTab_t {
    QByteArrayData data[1];
    char stringdata0[11];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_HistoryTab_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_HistoryTab_t qt_meta_stringdata_HistoryTab = {
    {
QT_MOC_LITERAL(0, 0, 10) // "HistoryTab"

    },
    "HistoryTab"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_HistoryTab[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

       0        // eod
};

void HistoryTab::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

QT_INIT_METAOBJECT const QMetaObject HistoryTab::staticMetaObject = { {
    QMetaObject::SuperData::link<GTab::staticMetaObject>(),
    qt_meta_stringdata_HistoryTab.data,
    qt_meta_data_HistoryTab,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *HistoryTab::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *HistoryTab::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_HistoryTab.stringdata0))
        return static_cast<void*>(this);
    return GTab::qt_metacast(_clname);
}

int HistoryTab::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = GTab::qt_metacall(_c, _id, _a);
    return _id;
}
struct qt_meta_stringdata_GroupDock_t {
    QByteArrayData data[22];
    char stringdata0[237];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_GroupDock_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_GroupDock_t qt_meta_stringdata_GroupDock = {
    {
QT_MOC_LITERAL(0, 0, 9), // "GroupDock"
QT_MOC_LITERAL(1, 10, 15), // "searchRequested"
QT_MOC_LITERAL(2, 26, 0), // ""
QT_MOC_LITERAL(3, 27, 4), // "name"
QT_MOC_LITERAL(4, 32, 12), // "SearchMethod"
QT_MOC_LITERAL(5, 45, 6), // "method"
QT_MOC_LITERAL(6, 52, 12), // "webRequested"
QT_MOC_LITERAL(7, 65, 3), // "url"
QT_MOC_LITERAL(8, 69, 14), // "pasteRequested"
QT_MOC_LITERAL(9, 84, 12), // "groupChanged"
QT_MOC_LITERAL(10, 97, 3), // "grp"
QT_MOC_LITERAL(11, 101, 11), // "bookChanged"
QT_MOC_LITERAL(12, 113, 5), // "index"
QT_MOC_LITERAL(13, 119, 17), // "bookViewRequested"
QT_MOC_LITERAL(14, 137, 5), // "Book*"
QT_MOC_LITERAL(15, 143, 4), // "book"
QT_MOC_LITERAL(16, 148, 17), // "fontViewRequested"
QT_MOC_LITERAL(17, 166, 13), // "menuRequested"
QT_MOC_LITERAL(18, 180, 13), // "fullRequested"
QT_MOC_LITERAL(19, 194, 15), // "changeGroupList"
QT_MOC_LITERAL(20, 210, 14), // "setCurrentBook"
QT_MOC_LITERAL(21, 225, 11) // "changeGroup"

    },
    "GroupDock\0searchRequested\0\0name\0"
    "SearchMethod\0method\0webRequested\0url\0"
    "pasteRequested\0groupChanged\0grp\0"
    "bookChanged\0index\0bookViewRequested\0"
    "Book*\0book\0fontViewRequested\0menuRequested\0"
    "fullRequested\0changeGroupList\0"
    "setCurrentBook\0changeGroup"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_GroupDock[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      12,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       9,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    2,   74,    2, 0x06 /* Public */,
       6,    2,   79,    2, 0x06 /* Public */,
       8,    2,   84,    2, 0x06 /* Public */,
       9,    1,   89,    2, 0x06 /* Public */,
      11,    1,   92,    2, 0x06 /* Public */,
      13,    1,   95,    2, 0x06 /* Public */,
      16,    1,   98,    2, 0x06 /* Public */,
      17,    0,  101,    2, 0x06 /* Public */,
      18,    0,  102,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      19,    0,  103,    2, 0x0a /* Public */,
      20,    1,  104,    2, 0x0a /* Public */,
      21,    1,  107,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString, 0x80000000 | 4,    3,    5,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    3,    7,
    QMetaType::Void, QMetaType::QString, 0x80000000 | 4,    3,    5,
    QMetaType::Void, QMetaType::Int,   10,
    QMetaType::Void, QMetaType::Int,   12,
    QMetaType::Void, 0x80000000 | 14,   15,
    QMetaType::Void, 0x80000000 | 14,   15,
    QMetaType::Void,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   12,
    QMetaType::Void, QMetaType::Int,   12,

       0        // eod
};

void GroupDock::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<GroupDock *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->searchRequested((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const SearchMethod(*)>(_a[2]))); break;
        case 1: _t->webRequested((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 2: _t->pasteRequested((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< const SearchMethod(*)>(_a[2]))); break;
        case 3: _t->groupChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->bookChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->bookViewRequested((*reinterpret_cast< Book*(*)>(_a[1]))); break;
        case 6: _t->fontViewRequested((*reinterpret_cast< Book*(*)>(_a[1]))); break;
        case 7: _t->menuRequested(); break;
        case 8: _t->fullRequested(); break;
        case 9: _t->changeGroupList(); break;
        case 10: _t->setCurrentBook((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 11: _t->changeGroup((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (GroupDock::*)(const QString & , const SearchMethod & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::searchRequested)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)(const QString & , const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::webRequested)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)(const QString & , const SearchMethod & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::pasteRequested)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::groupChanged)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::bookChanged)) {
                *result = 4;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)(Book * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::bookViewRequested)) {
                *result = 5;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)(Book * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::fontViewRequested)) {
                *result = 6;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::menuRequested)) {
                *result = 7;
                return;
            }
        }
        {
            using _t = void (GroupDock::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupDock::fullRequested)) {
                *result = 8;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject GroupDock::staticMetaObject = { {
    QMetaObject::SuperData::link<QDockWidget::staticMetaObject>(),
    qt_meta_stringdata_GroupDock.data,
    qt_meta_data_GroupDock,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *GroupDock::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GroupDock::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_GroupDock.stringdata0))
        return static_cast<void*>(this);
    return QDockWidget::qt_metacast(_clname);
}

int GroupDock::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDockWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 12)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 12;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 12)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 12;
    }
    return _id;
}

// SIGNAL 0
void GroupDock::searchRequested(const QString & _t1, const SearchMethod & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void GroupDock::webRequested(const QString & _t1, const QString & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void GroupDock::pasteRequested(const QString & _t1, const SearchMethod & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void GroupDock::groupChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}

// SIGNAL 4
void GroupDock::bookChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}

// SIGNAL 5
void GroupDock::bookViewRequested(Book * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 5, _a);
}

// SIGNAL 6
void GroupDock::fontViewRequested(Book * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 6, _a);
}

// SIGNAL 7
void GroupDock::menuRequested()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void GroupDock::fullRequested()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
