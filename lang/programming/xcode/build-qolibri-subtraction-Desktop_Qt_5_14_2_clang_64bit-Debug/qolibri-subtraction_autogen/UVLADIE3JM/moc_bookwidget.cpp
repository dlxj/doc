/****************************************************************************
** Meta object code from reading C++ file 'bookwidget.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "bookwidget.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'bookwidget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_BookWidget_t {
    QByteArrayData data[20];
    char stringdata0[185];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_BookWidget_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_BookWidget_t qt_meta_stringdata_BookWidget = {
    {
QT_MOC_LITERAL(0, 0, 10), // "BookWidget"
QT_MOC_LITERAL(1, 11, 10), // "rowChanged"
QT_MOC_LITERAL(2, 22, 0), // ""
QT_MOC_LITERAL(3, 23, 3), // "row"
QT_MOC_LITERAL(4, 27, 17), // "bookViewRequested"
QT_MOC_LITERAL(5, 45, 5), // "Book*"
QT_MOC_LITERAL(6, 51, 4), // "book"
QT_MOC_LITERAL(7, 56, 17), // "fontViewRequested"
QT_MOC_LITERAL(8, 74, 6), // "upItem"
QT_MOC_LITERAL(9, 81, 8), // "downItem"
QT_MOC_LITERAL(10, 90, 7), // "delItem"
QT_MOC_LITERAL(11, 98, 8), // "viewItem"
QT_MOC_LITERAL(12, 107, 8), // "editItem"
QT_MOC_LITERAL(13, 116, 16), // "QListWidgetItem*"
QT_MOC_LITERAL(14, 133, 4), // "item"
QT_MOC_LITERAL(15, 138, 7), // "setFont"
QT_MOC_LITERAL(16, 146, 9), // "changeRow"
QT_MOC_LITERAL(17, 156, 10), // "changeName"
QT_MOC_LITERAL(18, 167, 12), // "changeSelect"
QT_MOC_LITERAL(19, 180, 4) // "prev"

    },
    "BookWidget\0rowChanged\0\0row\0bookViewRequested\0"
    "Book*\0book\0fontViewRequested\0upItem\0"
    "downItem\0delItem\0viewItem\0editItem\0"
    "QListWidgetItem*\0item\0setFont\0changeRow\0"
    "changeName\0changeSelect\0prev"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_BookWidget[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      13,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   79,    2, 0x06 /* Public */,
       4,    1,   82,    2, 0x06 /* Public */,
       7,    1,   85,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       8,    0,   88,    2, 0x08 /* Private */,
       9,    0,   89,    2, 0x08 /* Private */,
      10,    0,   90,    2, 0x08 /* Private */,
      11,    0,   91,    2, 0x08 /* Private */,
      12,    1,   92,    2, 0x08 /* Private */,
      12,    0,   95,    2, 0x08 /* Private */,
      15,    0,   96,    2, 0x08 /* Private */,
      16,    0,   97,    2, 0x08 /* Private */,
      17,    1,   98,    2, 0x08 /* Private */,
      18,    2,  101,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void, 0x80000000 | 5,    6,
    QMetaType::Void, 0x80000000 | 5,    6,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 13,   14,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 13,   14,
    QMetaType::Void, 0x80000000 | 13, 0x80000000 | 13,    2,   19,

       0        // eod
};

void BookWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<BookWidget *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->rowChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->bookViewRequested((*reinterpret_cast< Book*(*)>(_a[1]))); break;
        case 2: _t->fontViewRequested((*reinterpret_cast< Book*(*)>(_a[1]))); break;
        case 3: _t->upItem(); break;
        case 4: _t->downItem(); break;
        case 5: _t->delItem(); break;
        case 6: _t->viewItem(); break;
        case 7: _t->editItem((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 8: _t->editItem(); break;
        case 9: _t->setFont(); break;
        case 10: _t->changeRow(); break;
        case 11: _t->changeName((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 12: _t->changeSelect((*reinterpret_cast< QListWidgetItem*(*)>(_a[1])),(*reinterpret_cast< QListWidgetItem*(*)>(_a[2]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (BookWidget::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookWidget::rowChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (BookWidget::*)(Book * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookWidget::bookViewRequested)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (BookWidget::*)(Book * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookWidget::fontViewRequested)) {
                *result = 2;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject BookWidget::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_meta_stringdata_BookWidget.data,
    qt_meta_data_BookWidget,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *BookWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *BookWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_BookWidget.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int BookWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 13)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 13;
    }
    return _id;
}

// SIGNAL 0
void BookWidget::rowChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void BookWidget::bookViewRequested(Book * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void BookWidget::fontViewRequested(Book * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
