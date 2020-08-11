/****************************************************************************
** Meta object code from reading C++ file 'groupwidget.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "groupwidget.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'groupwidget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_GroupWidget_t {
    QByteArrayData data[18];
    char stringdata0[163];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_GroupWidget_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_GroupWidget_t qt_meta_stringdata_GroupWidget = {
    {
QT_MOC_LITERAL(0, 0, 11), // "GroupWidget"
QT_MOC_LITERAL(1, 12, 10), // "rowChanged"
QT_MOC_LITERAL(2, 23, 0), // ""
QT_MOC_LITERAL(3, 24, 3), // "row"
QT_MOC_LITERAL(4, 28, 9), // "initGroup"
QT_MOC_LITERAL(5, 38, 14), // "changeAddGroup"
QT_MOC_LITERAL(6, 53, 3), // "str"
QT_MOC_LITERAL(7, 57, 11), // "createGroup"
QT_MOC_LITERAL(8, 69, 6), // "upItem"
QT_MOC_LITERAL(9, 76, 8), // "downItem"
QT_MOC_LITERAL(10, 85, 7), // "delItem"
QT_MOC_LITERAL(11, 93, 9), // "changeRow"
QT_MOC_LITERAL(12, 103, 8), // "editItem"
QT_MOC_LITERAL(13, 112, 16), // "QListWidgetItem*"
QT_MOC_LITERAL(14, 129, 4), // "item"
QT_MOC_LITERAL(15, 134, 10), // "changeName"
QT_MOC_LITERAL(16, 145, 12), // "changeSelect"
QT_MOC_LITERAL(17, 158, 4) // "prev"

    },
    "GroupWidget\0rowChanged\0\0row\0initGroup\0"
    "changeAddGroup\0str\0createGroup\0upItem\0"
    "downItem\0delItem\0changeRow\0editItem\0"
    "QListWidgetItem*\0item\0changeName\0"
    "changeSelect\0prev"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_GroupWidget[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      12,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   74,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       4,    0,   77,    2, 0x08 /* Private */,
       5,    1,   78,    2, 0x08 /* Private */,
       7,    0,   81,    2, 0x08 /* Private */,
       8,    0,   82,    2, 0x08 /* Private */,
       9,    0,   83,    2, 0x08 /* Private */,
      10,    0,   84,    2, 0x08 /* Private */,
      11,    1,   85,    2, 0x08 /* Private */,
      12,    1,   88,    2, 0x08 /* Private */,
      12,    0,   91,    2, 0x08 /* Private */,
      15,    1,   92,    2, 0x08 /* Private */,
      16,    2,   95,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    3,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,    6,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, 0x80000000 | 13,   14,
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 13,   14,
    QMetaType::Void, 0x80000000 | 13, 0x80000000 | 13,    2,   17,

       0        // eod
};

void GroupWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<GroupWidget *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->rowChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->initGroup(); break;
        case 2: _t->changeAddGroup((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->createGroup(); break;
        case 4: _t->upItem(); break;
        case 5: _t->downItem(); break;
        case 6: _t->delItem(); break;
        case 7: _t->changeRow((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->editItem((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 9: _t->editItem(); break;
        case 10: _t->changeName((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 11: _t->changeSelect((*reinterpret_cast< QListWidgetItem*(*)>(_a[1])),(*reinterpret_cast< QListWidgetItem*(*)>(_a[2]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (GroupWidget::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&GroupWidget::rowChanged)) {
                *result = 0;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject GroupWidget::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_meta_stringdata_GroupWidget.data,
    qt_meta_data_GroupWidget,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *GroupWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GroupWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_GroupWidget.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int GroupWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
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
void GroupWidget::rowChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
