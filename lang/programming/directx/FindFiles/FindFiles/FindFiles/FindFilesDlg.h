// FindFilesDlg.h : header file
//

#if !defined(__FINDFILESDLG_H__)
#define __FINDFILESDLG_H__

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "FileFinder.h"

/////////////////////////////////////////////////////////////////////////////
// CFindFilesDlg dialog

class CFindFilesDlg : public CDialog
{
// Construction
public:
	CFindFilesDlg(CWnd* pParent = NULL);	// standard constructor

	void	AddFileToList(LPCTSTR szFilename);
	CString	GetListFilename(int nIndex);
	int		FindInList(LPCTSTR szFilename);
	void	SetStatus(int nCount = 0, LPCTSTR szFolder = NULL);

// Dialog Data
	//{{AFX_DATA(CFindFilesDlg)
	enum { IDD = IDD_FINDFILES_DIALOG };
	CListCtrl	m_list;
	BOOL	m_bSize;
	BOOL	m_bSubFolders;
	CString	m_sFileMask;
	long	m_nMaxSize;
	long	m_nMinSize;
	CString	m_sBaseFolder;
	CString	m_sFindText;
	int		m_nSearchType;
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CFindFilesDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	static void FileFinderProc(CFileFinder *pFinder, DWORD dwCode, void *pCustomParam);

	// Generated message map functions
	//{{AFX_MSG(CFindFilesDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg int OnCreate(LPCREATESTRUCT lpCreateStruct);
	afx_msg void OnGetMinMaxInfo(MINMAXINFO FAR* lpMMI);
	afx_msg void OnSize(UINT nType, int cx, int cy);
	afx_msg void OnCheckSize();
	afx_msg void OnSearch();
	virtual void OnCancel();
	afx_msg void OnBrowse();
	afx_msg void OnDblclkList(NMHDR* pNMHDR, LRESULT* pResult);
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()

private:
	CImageList	_imgList;
	bool		_bSearching;
	CFileFinder	_finder;
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(__FINDFILESDLG_H__)
