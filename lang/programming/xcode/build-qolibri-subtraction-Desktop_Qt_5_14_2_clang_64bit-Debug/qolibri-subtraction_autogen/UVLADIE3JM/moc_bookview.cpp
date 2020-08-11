/****************************************************************************
** Meta object code from reading C++ file 'bookview.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "bookview.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'bookview.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_BookView_t {
    QByteArrayData data[26];
    char stringdata0[318];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_BookView_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_BookView_t qt_meta_stringdata_BookView = {
    {
QT_MOC_LITERAL(0, 0, 8), // "BookView"
QT_MOC_LITERAL(1, 9, 15), // "searchRequested"
QT_MOC_LITERAL(2, 25, 0), // ""
QT_MOC_LITERAL(3, 26, 15), // "SearchDirection"
QT_MOC_LITERAL(4, 42, 14), // "pasteRequested"
QT_MOC_LITERAL(5, 57, 14), // "soundRequested"
QT_MOC_LITERAL(6, 72, 14), // "videoRequested"
QT_MOC_LITERAL(7, 87, 8), // "fileName"
QT_MOC_LITERAL(8, 96, 21), // "externalLinkRequested"
QT_MOC_LITERAL(9, 118, 18), // "selectionRequested"
QT_MOC_LITERAL(10, 137, 15), // "popupBrowserSet"
QT_MOC_LITERAL(11, 153, 11), // "fontChanged"
QT_MOC_LITERAL(12, 165, 15), // "statusRequested"
QT_MOC_LITERAL(13, 181, 10), // "tabChanged"
QT_MOC_LITERAL(14, 192, 9), // "tab_count"
QT_MOC_LITERAL(15, 202, 12), // "allWebLoaded"
QT_MOC_LITERAL(16, 215, 14), // "showTabBarMenu"
QT_MOC_LITERAL(17, 230, 3), // "pnt"
QT_MOC_LITERAL(18, 234, 8), // "closeTab"
QT_MOC_LITERAL(19, 243, 11), // "closeAllTab"
QT_MOC_LITERAL(20, 255, 10), // "stopSearch"
QT_MOC_LITERAL(21, 266, 6), // "zoomIn"
QT_MOC_LITERAL(22, 273, 7), // "zoomOut"
QT_MOC_LITERAL(23, 281, 14), // "viewTabChanged"
QT_MOC_LITERAL(24, 296, 5), // "index"
QT_MOC_LITERAL(25, 302, 15) // "webViewFinished"

    },
    "BookView\0searchRequested\0\0SearchDirection\0"
    "pasteRequested\0soundRequested\0"
    "videoRequested\0fileName\0externalLinkRequested\0"
    "selectionRequested\0popupBrowserSet\0"
    "fontChanged\0statusRequested\0tabChanged\0"
    "tab_count\0allWebLoaded\0showTabBarMenu\0"
    "pnt\0closeTab\0closeAllTab\0stopSearch\0"
    "zoomIn\0zoomOut\0viewTabChanged\0index\0"
    "webViewFinished"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_BookView[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      19,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
      11,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    2,  109,    2, 0x06 /* Public */,
       4,    1,  114,    2, 0x06 /* Public */,
       5,    1,  117,    2, 0x06 /* Public */,
       6,    1,  120,    2, 0x06 /* Public */,
       8,    1,  123,    2, 0x06 /* Public */,
       9,    1,  126,    2, 0x06 /* Public */,
      10,    1,  129,    2, 0x06 /* Public */,
      11,    1,  132,    2, 0x06 /* Public */,
      12,    1,  135,    2, 0x06 /* Public */,
      13,    1,  138,    2, 0x06 /* Public */,
      15,    0,  141,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      16,    1,  142,    2, 0x08 /* Private */,
      18,    0,  145,    2, 0x08 /* Private */,
      19,    0,  146,    2, 0x08 /* Private */,
      20,    0,  147,    2, 0x08 /* Private */,
      21,    0,  148,    2, 0x08 /* Private */,
      22,    0,  149,    2, 0x08 /* Private */,
      23,    1,  150,    2, 0x08 /* Private */,
      25,    1,  153,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QString,    2,    2,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::QString,    7,
    QMetaType::Void, QMetaType::QString,    7,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QFont,    2,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::Int,   14,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void, QMetaType::QPoint,   17,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   24,
    QMetaType::Void, QMetaType::Bool,    2,

       0        // eod
};

void BookView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<BookView *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->searchRequested((*reinterpret_cast< SearchDirection(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 1: _t->pasteRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->soundRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->videoRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->externalLinkRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->selectionRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 6: _t->popupBrowserSet((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->fontChanged((*reinterpret_cast< const QFont(*)>(_a[1]))); break;
        case 8: _t->statusRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 9: _t->tabChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 10: _t->allWebLoaded(); break;
        case 11: _t->showTabBarMenu((*reinterpret_cast< const QPoint(*)>(_a[1]))); break;
        case 12: _t->closeTab(); break;
        case 13: _t->closeAllTab(); break;
        case 14: _t->stopSearch(); break;
        case 15: _t->zoomIn(); break;
        case 16: _t->zoomOut(); break;
        case 17: _t->viewTabChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 18: _t->webViewFinished((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (BookView::*)(SearchDirection , const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::searchRequested)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (BookView::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::pasteRequested)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (BookView::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::soundRequested)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (BookView::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::videoRequested)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (BookView::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::externalLinkRequested)) {
                *result = 4;
                return;
            }
        }
        {
            using _t = void (BookView::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::selectionRequested)) {
                *result = 5;
                return;
            }
        }
        {
            using _t = void (BookView::*)(bool );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::popupBrowserSet)) {
                *result = 6;
                return;
            }
        }
        {
            using _t = void (BookView::*)(const QFont & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::fontChanged)) {
                *result = 7;
                return;
            }
        }
        {
            using _t = void (BookView::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::statusRequested)) {
                *result = 8;
                return;
            }
        }
        {
            using _t = void (BookView::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::tabChanged)) {
                *result = 9;
                return;
            }
        }
        {
            using _t = void (BookView::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&BookView::allWebLoaded)) {
                *result = 10;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject BookView::staticMetaObject = { {
    QMetaObject::SuperData::link<QTabWidget::staticMetaObject>(),
    qt_meta_stringdata_BookView.data,
    qt_meta_data_BookView,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *BookView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *BookView::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_BookView.stringdata0))
        return static_cast<void*>(this);
    return QTabWidget::qt_metacast(_clname);
}

int BookView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QTabWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 19)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 19;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 19)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 19;
    }
    return _id;
}

// SIGNAL 0
void BookView::searchRequested(SearchDirection _t1, const QString & _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void BookView::pasteRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void BookView::soundRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void BookView::videoRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}

// SIGNAL 4
void BookView::externalLinkRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}

// SIGNAL 5
void BookView::selectionRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 5, _a);
}

// SIGNAL 6
void BookView::popupBrowserSet(bool _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 6, _a);
}

// SIGNAL 7
void BookView::fontChanged(const QFont & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 7, _a);
}

// SIGNAL 8
void BookView::statusRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 8, _a);
}

// SIGNAL 9
void BookView::tabChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 9, _a);
}

// SIGNAL 10
void BookView::allWebLoaded()
{
    QMetaObject::activate(this, &staticMetaObject, 10, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
