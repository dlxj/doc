/****************************************************************************
** Meta object code from reading C++ file 'bookbrowser.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "bookbrowser.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'bookbrowser.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_BookBrowser_t {
    QByteArrayData data[15];
    char stringdata0[202];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_BookBrowser_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_BookBrowser_t qt_meta_stringdata_BookBrowser = {
    {
QT_MOC_LITERAL(0, 0, 11), // "BookBrowser"
QT_MOC_LITERAL(1, 12, 15), // "searchRequested"
QT_MOC_LITERAL(2, 28, 0), // ""
QT_MOC_LITERAL(3, 29, 15), // "SearchDirection"
QT_MOC_LITERAL(4, 45, 14), // "pasteRequested"
QT_MOC_LITERAL(5, 60, 14), // "soundRequested"
QT_MOC_LITERAL(6, 75, 5), // "fname"
QT_MOC_LITERAL(7, 81, 14), // "videoRequested"
QT_MOC_LITERAL(8, 96, 8), // "fileName"
QT_MOC_LITERAL(9, 105, 21), // "externalLinkRequested"
QT_MOC_LITERAL(10, 127, 18), // "selectionRequested"
QT_MOC_LITERAL(11, 146, 3), // "str"
QT_MOC_LITERAL(12, 150, 15), // "statusRequested"
QT_MOC_LITERAL(13, 166, 19), // "changeTextSelection"
QT_MOC_LITERAL(14, 186, 15) // "pasteSearchText"

    },
    "BookBrowser\0searchRequested\0\0"
    "SearchDirection\0pasteRequested\0"
    "soundRequested\0fname\0videoRequested\0"
    "fileName\0externalLinkRequested\0"
    "selectionRequested\0str\0statusRequested\0"
    "changeTextSelection\0pasteSearchText"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_BookBrowser[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       9,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       7,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    2,   59,    2, 0x06 /* Public */,
       4,    1,   64,    2, 0x06 /* Public */,
       5,    1,   67,    2, 0x06 /* Public */,
       7,    1,   70,    2, 0x06 /* Public */,
       9,    1,   73,    2, 0x06 /* Public */,
      10,    1,   76,    2, 0x06 /* Public */,
      12,    1,   79,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      13,    0,   82,    2, 0x08 /* Private */,
      14,    0,   83,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QString,    2,    2,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::QString,    6,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, QMetaType::QString,   11,
    QMetaType::Void, QMetaType::QString,   11,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void BookBrowser::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<BookBrowser *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->searchRequested((*reinterpret_cast< SearchDirection(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 1: _t->pasteRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->soundRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->videoRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->externalLinkRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->selectionRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 6: _t->statusRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 7: _t->changeTextSelection(); break;
        case 8: _t->pasteSearchText(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (BookBrowser::*)(SearchDirection , const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookBrowser::searchRequested)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (BookBrowser::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookBrowser::pasteRequested)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (BookBrowser::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookBrowser::soundRequested)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (BookBrowser::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookBrowser::videoRequested)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (BookBrowser::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookBrowser::externalLinkRequested)) {
                *result = 4;
                return;
            }
        }
        {
            using _t = void (BookBrowser::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookBrowser::selectionRequested)) {
                *result = 5;
                return;
            }
        }
        {
            using _t = void (BookBrowser::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookBrowser::statusRequested)) {
                *result = 6;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject BookBrowser::staticMetaObject = { {
    QMetaObject::SuperData::link<QTextBrowser::staticMetaObject>(),
    qt_meta_stringdata_BookBrowser.data,
    qt_meta_data_BookBrowser,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *BookBrowser::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *BookBrowser::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_BookBrowser.stringdata0))
        return static_cast<void*>(this);
    return QTextBrowser::qt_metacast(_clname);
}

int BookBrowser::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QTextBrowser::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 9)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 9;
    }
    return _id;
}

// SIGNAL 0
void BookBrowser::searchRequested(SearchDirection _t1, const QString & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void BookBrowser::pasteRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void BookBrowser::soundRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void BookBrowser::videoRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}

// SIGNAL 4
void BookBrowser::externalLinkRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}

// SIGNAL 5
void BookBrowser::selectionRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 5, _a);
}

// SIGNAL 6
void BookBrowser::statusRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 6, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
