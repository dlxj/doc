/****************************************************************************
** Meta object code from reading C++ file 'pagewidget.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "pagewidget.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'pagewidget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_PageWidget_t {
    QByteArrayData data[14];
    char stringdata0[138];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_PageWidget_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_PageWidget_t qt_meta_stringdata_PageWidget = {
    {
QT_MOC_LITERAL(0, 0, 10), // "PageWidget"
QT_MOC_LITERAL(1, 11, 15), // "statusRequested"
QT_MOC_LITERAL(2, 27, 0), // ""
QT_MOC_LITERAL(3, 28, 3), // "str"
QT_MOC_LITERAL(4, 32, 18), // "selectionRequested"
QT_MOC_LITERAL(5, 51, 18), // "setBookTreeVisible"
QT_MOC_LITERAL(6, 70, 7), // "visible"
QT_MOC_LITERAL(7, 78, 8), // "scrollTo"
QT_MOC_LITERAL(8, 87, 16), // "QTreeWidgetItem*"
QT_MOC_LITERAL(9, 104, 2), // "to"
QT_MOC_LITERAL(10, 107, 10), // "changeFont"
QT_MOC_LITERAL(11, 118, 4), // "font"
QT_MOC_LITERAL(12, 123, 10), // "popupSlide"
QT_MOC_LITERAL(13, 134, 3) // "pos"

    },
    "PageWidget\0statusRequested\0\0str\0"
    "selectionRequested\0setBookTreeVisible\0"
    "visible\0scrollTo\0QTreeWidgetItem*\0to\0"
    "changeFont\0font\0popupSlide\0pos"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_PageWidget[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       7,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   49,    2, 0x06 /* Public */,
       4,    1,   52,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       5,    1,   55,    2, 0x0a /* Public */,
       7,    2,   58,    2, 0x08 /* Private */,
       7,    2,   63,    2, 0x08 /* Private */,
      10,    1,   68,    2, 0x08 /* Private */,
      12,    1,   71,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString,    3,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    6,
    QMetaType::Void, 0x80000000 | 8, QMetaType::Int,    9,    2,
    QMetaType::Void, 0x80000000 | 8, 0x80000000 | 8,    9,    2,
    QMetaType::Void, QMetaType::QFont,   11,
    QMetaType::Void, QMetaType::QPoint,   13,

       0        // eod
};

void PageWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<PageWidget *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->statusRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->selectionRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->setBookTreeVisible((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->scrollTo((*reinterpret_cast< QTreeWidgetItem*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 4: _t->scrollTo((*reinterpret_cast< QTreeWidgetItem*(*)>(_a[1])),(*reinterpret_cast< QTreeWidgetItem*(*)>(_a[2]))); break;
        case 5: _t->changeFont((*reinterpret_cast< const QFont(*)>(_a[1]))); break;
        case 6: _t->popupSlide((*reinterpret_cast< const QPoint(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (PageWidget::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&PageWidget::statusRequested)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (PageWidget::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&PageWidget::selectionRequested)) {
                *result = 1;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject PageWidget::staticMetaObject = { {
    QMetaObject::SuperData::link<QSplitter::staticMetaObject>(),
    qt_meta_stringdata_PageWidget.data,
    qt_meta_data_PageWidget,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *PageWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *PageWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_PageWidget.stringdata0))
        return static_cast<void*>(this);
    return QSplitter::qt_metacast(_clname);
}

int PageWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSplitter::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 7)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 7;
    }
    return _id;
}

// SIGNAL 0
void PageWidget::statusRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void PageWidget::selectionRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
