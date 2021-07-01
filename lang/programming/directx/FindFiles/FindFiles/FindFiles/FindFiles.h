// FindFiles.h : main header file for the FINDFILES application
//

#if !defined(AFX_FINDFILES_H__975DBCAB_3FF9_4048_B476_8EA1D2F8073D__INCLUDED_)
#define AFX_FINDFILES_H__975DBCAB_3FF9_4048_B476_8EA1D2F8073D__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CFindFilesApp:
// See FindFiles.cpp for the implementation of this class
//

class CFindFilesApp : public CWinApp
{
public:
	CFindFilesApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CFindFilesApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CFindFilesApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_FINDFILES_H__975DBCAB_3FF9_4048_B476_8EA1D2F8073D__INCLUDED_)
