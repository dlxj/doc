#ifndef GLOBALEVENTFILTER_H
#define GLOBALEVENTFILTER_H

#include <QEvent>
#include <QObject>

class GlobalEventFilter : public QObject
{
	Q_OBJECT

protected:
	bool eventFilter(QObject *obj, QEvent *event);

signals:
	void focusSearch();
};

#endif // GLOBALEVENTFILTER_H
