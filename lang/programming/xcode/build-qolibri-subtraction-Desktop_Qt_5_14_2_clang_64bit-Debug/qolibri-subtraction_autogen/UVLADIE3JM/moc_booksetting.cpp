/****************************************************************************
** Meta object code from reading C++ file 'booksetting.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "booksetting.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'booksetting.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_WebSetting_t {
    QByteArrayData data[4];
    char stringdata0[29];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_WebSetting_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_WebSetting_t qt_meta_stringdata_WebSetting = {
    {
QT_MOC_LITERAL(0, 0, 10), // "WebSetting"
QT_MOC_LITERAL(1, 11, 11), // "setOkButton"
QT_MOC_LITERAL(2, 23, 0), // ""
QT_MOC_LITERAL(3, 24, 4) // "text"

    },
    "WebSetting\0setOkButton\0\0text"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_WebSetting[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   19,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    3,

       0        // eod
};

void WebSetting::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<WebSetting *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->setOkButton((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject WebSetting::staticMetaObject = { {
    QMetaObject::SuperData::link<QDialog::staticMetaObject>(),
    qt_meta_stringdata_WebSetting.data,
    qt_meta_data_WebSetting,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *WebSetting::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *WebSetting::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_WebSetting.stringdata0))
        return static_cast<void*>(this);
    return QDialog::qt_metacast(_clname);
}

int WebSetting::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 1;
    }
    return _id;
}
struct qt_meta_stringdata_EpwingFileSetting_t {
    QByteArrayData data[4];
    char stringdata0[36];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_EpwingFileSetting_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_EpwingFileSetting_t qt_meta_stringdata_EpwingFileSetting = {
    {
QT_MOC_LITERAL(0, 0, 17), // "EpwingFileSetting"
QT_MOC_LITERAL(1, 18, 11), // "setOkButton"
QT_MOC_LITERAL(2, 30, 0), // ""
QT_MOC_LITERAL(3, 31, 4) // "text"

    },
    "EpwingFileSetting\0setOkButton\0\0text"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_EpwingFileSetting[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   19,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    3,

       0        // eod
};

void EpwingFileSetting::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<EpwingFileSetting *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->setOkButton((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject EpwingFileSetting::staticMetaObject = { {
    QMetaObject::SuperData::link<QDialog::staticMetaObject>(),
    qt_meta_stringdata_EpwingFileSetting.data,
    qt_meta_data_EpwingFileSetting,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *EpwingFileSetting::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *EpwingFileSetting::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_EpwingFileSetting.stringdata0))
        return static_cast<void*>(this);
    return QDialog::qt_metacast(_clname);
}

int EpwingFileSetting::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 1;
    }
    return _id;
}
struct qt_meta_stringdata_BookSetting_t {
    QByteArrayData data[19];
    char stringdata0[201];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_BookSetting_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_BookSetting_t qt_meta_stringdata_BookSetting = {
    {
QT_MOC_LITERAL(0, 0, 11), // "BookSetting"
QT_MOC_LITERAL(1, 12, 6), // "accept"
QT_MOC_LITERAL(2, 19, 0), // ""
QT_MOC_LITERAL(3, 20, 10), // "searchBook"
QT_MOC_LITERAL(4, 31, 12), // "cancelSearch"
QT_MOC_LITERAL(5, 44, 9), // "changeTab"
QT_MOC_LITERAL(6, 54, 5), // "index"
QT_MOC_LITERAL(7, 60, 17), // "searchPathChanged"
QT_MOC_LITERAL(8, 78, 3), // "str"
QT_MOC_LITERAL(9, 82, 14), // "webNameChanged"
QT_MOC_LITERAL(10, 97, 14), // "webSiteChanged"
QT_MOC_LITERAL(11, 112, 8), // "editItem"
QT_MOC_LITERAL(12, 121, 7), // "addItem"
QT_MOC_LITERAL(13, 129, 7), // "addBook"
QT_MOC_LITERAL(14, 137, 10), // "addWebSite"
QT_MOC_LITERAL(15, 148, 20), // "changeGroupSelection"
QT_MOC_LITERAL(16, 169, 3), // "row"
QT_MOC_LITERAL(17, 173, 19), // "changeBookSelection"
QT_MOC_LITERAL(18, 193, 7) // "setPath"

    },
    "BookSetting\0accept\0\0searchBook\0"
    "cancelSearch\0changeTab\0index\0"
    "searchPathChanged\0str\0webNameChanged\0"
    "webSiteChanged\0editItem\0addItem\0addBook\0"
    "addWebSite\0changeGroupSelection\0row\0"
    "changeBookSelection\0setPath"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_BookSetting[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      14,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   84,    2, 0x0a /* Public */,
       3,    0,   85,    2, 0x08 /* Private */,
       4,    0,   86,    2, 0x08 /* Private */,
       5,    1,   87,    2, 0x08 /* Private */,
       7,    1,   90,    2, 0x08 /* Private */,
       9,    1,   93,    2, 0x08 /* Private */,
      10,    1,   96,    2, 0x08 /* Private */,
      11,    0,   99,    2, 0x08 /* Private */,
      12,    0,  100,    2, 0x08 /* Private */,
      13,    0,  101,    2, 0x08 /* Private */,
      14,    0,  102,    2, 0x08 /* Private */,
      15,    1,  103,    2, 0x08 /* Private */,
      17,    1,  106,    2, 0x08 /* Private */,
      18,    0,  109,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    6,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   16,
    QMetaType::Void, QMetaType::Int,   16,
    QMetaType::Void,

       0        // eod
};

void BookSetting::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<BookSetting *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->accept(); break;
        case 1: _t->searchBook(); break;
        case 2: _t->cancelSearch(); break;
        case 3: _t->changeTab((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->searchPathChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->webNameChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 6: _t->webSiteChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 7: _t->editItem(); break;
        case 8: _t->addItem(); break;
        case 9: _t->addBook(); break;
        case 10: _t->addWebSite(); break;
        case 11: _t->changeGroupSelection((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 12: _t->changeBookSelection((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 13: _t->setPath(); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject BookSetting::staticMetaObject = { {
    QMetaObject::SuperData::link<QDialog::staticMetaObject>(),
    qt_meta_stringdata_BookSetting.data,
    qt_meta_data_BookSetting,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *BookSetting::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *BookSetting::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_BookSetting.stringdata0))
        return static_cast<void*>(this);
    return QDialog::qt_metacast(_clname);
}

int BookSetting::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 14)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 14;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 14)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 14;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
