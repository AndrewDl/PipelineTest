/* GStreamer
 * Copyright (C) 2004 Thomas Vander Stichele <thomas@apestaart.org>
 *
 * gst-i18n-app.h: internationalization macros for the GStreamer tools
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */


#ifndef __GST_I18N_APP_H__
#define __GST_I18N_APP_H__

#ifdef ENABLE_NLS
#include "gettext.h" /* included with gettext distribution and copied */

/* we want to use shorthand _() for translating and N_() for marking */
#define _(String) gettext (String)
#define N_(String) gettext_noop (String)
/* FIXME: if we need it, we can add Q_ as well, like in glib */

#else

#define _(String) String
#define N_(String) String

#endif

#endif /* __GST_I18N_APP_H__ */
