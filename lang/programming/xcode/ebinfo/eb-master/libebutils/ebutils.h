/* automatically generated from ebutils.h.in. */
/*                                                            -*- C -*-
 * Copyright (c) 2000-2006  Motoyuki Kasahara
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef EBUTILS_H
#define EBUTILS_H

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "eb/eb.h"

/*
 * Text domain name for message catalog.
 */
#define TEXT_DOMAIN_NAME	"ebutils"

/*
 * Path to the locale directory.
 */
#ifndef WIN32
#define LOCALEDIR		"/usr/local/share/locale"
#else
#define LOCALEDIR		localedir()
#endif

/*
 * Function declarations.
 */
/* ebutils.c */
void output_try_help(const char *invoked_name);
void output_version(const char *program_name, const char *program_version);
int parse_subbook_name_argument(const char *invoked_name, const char *argument,
    char name_list[][EB_MAX_DIRECTORY_NAME_LENGTH  + 1], int *name_count);
EB_Subbook_Code find_subbook(EB_Book *book, const char *directory,
    EB_Subbook_Code *subbook_code);
void canonicalize_path(char *path);

/* puts_eucjp.c */
int fputs_eucjp_to_locale(const char *string, FILE *stream);
int puts_eucjp_to_locale(const char *string);

#endif /* not EBUTILS_H */
