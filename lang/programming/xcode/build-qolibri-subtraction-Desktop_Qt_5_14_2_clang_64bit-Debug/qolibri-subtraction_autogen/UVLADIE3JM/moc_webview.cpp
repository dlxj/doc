/****************************************************************************
** Meta object code from reading C++ file 'webview.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "webview.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'webview.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_WebView_t {
    QByteArrayData data[16];
    char stringdata0[158];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_WebView_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_WebView_t qt_meta_stringdata_WebView = {
    {
QT_MOC_LITERAL(0, 0, 7), // "WebView"
QT_MOC_LITERAL(1, 8, 21), // "externalLinkRequested"
QT_MOC_LITERAL(2, 30, 0), // ""
QT_MOC_LITERAL(3, 31, 3), // "url"
QT_MOC_LITERAL(4, 35, 13), // "progressStart"
QT_MOC_LITERAL(5, 49, 8), // "progress"
QT_MOC_LITERAL(6, 58, 6), // "pcount"
QT_MOC_LITERAL(7, 65, 16), // "progressFinished"
QT_MOC_LITERAL(8, 82, 2), // "ok"
QT_MOC_LITERAL(9, 85, 8), // "openLink"
QT_MOC_LITERAL(10, 94, 10), // "openNewWin"
QT_MOC_LITERAL(11, 105, 15), // "copyHoveredLink"
QT_MOC_LITERAL(12, 121, 4), // "link"
QT_MOC_LITERAL(13, 126, 10), // "changeFont"
QT_MOC_LITERAL(14, 137, 4), // "font"
QT_MOC_LITERAL(15, 142, 15) // "setPopupBrowser"

    },
    "WebView\0externalLinkRequested\0\0url\0"
    "progressStart\0progress\0pcount\0"
    "progressFinished\0ok\0openLink\0openNewWin\0"
    "copyHoveredLink\0link\0changeFont\0font\0"
    "setPopupBrowser"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_WebView[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       9,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   59,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       4,    0,   62,    2, 0x08 /* Private */,
       5,    1,   63,    2, 0x08 /* Private */,
       7,    1,   66,    2, 0x08 /* Private */,
       9,    1,   69,    2, 0x08 /* Private */,
      10,    0,   72,    2, 0x08 /* Private */,
      11,    1,   73,    2, 0x08 /* Private */,
      13,    1,   76,    2, 0x08 /* Private */,
      15,    1,   79,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString,    3,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    6,
    QMetaType::Void, QMetaType::Bool,    8,
    QMetaType::Void, QMetaType::QUrl,    3,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,   12,
    QMetaType::Void, QMetaType::QFont,   14,
    QMetaType::Void, QMetaType::Bool,    2,

       0        // eod
};

void WebView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<WebView *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->externalLinkRequested((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->progressStart(); break;
        case 2: _t->progress((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->progressFinished((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->openLink((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        case 5: _t->openNewWin(); break;
        case 6: _t->copyHoveredLink((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 7: _t->changeFont((*reinterpret_cast< const QFont(*)>(_a[1]))); break;
        case 8: _t->setPopupBrowser((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (WebView::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&WebView::externalLinkRequested)) {
                *result = 0;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject WebView::staticMetaObject = { {
    QMetaObject::SuperData::link<QWebEngineView::staticMetaObject>(),
    qt_meta_stringdata_WebView.data,
    qt_meta_data_WebView,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *WebView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *WebView::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_WebView.stringdata0))
        return static_cast<void*>(this);
    return QWebEngineView::qt_metacast(_clname);
}

int WebView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWebEngineView::qt_metacall(_c, _id, _a);
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
void WebView::externalLinkRequested(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
