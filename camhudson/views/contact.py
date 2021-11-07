"""Cam Hudson Personal Website app's contact-info.html view.

URLs handled in this file include:
/contact-info
"""
from datetime import datetime
from flask.templating import render_template
from camhudson.views.utility import create_contact_info_card  # Make linter shut up
import camhudson

@camhudson.app.route('/contact-info', methods=['GET'])
def get_contact_info() -> str:
    """Handle request for homepage."""
    current_hour = datetime.now().time().hour
    time_of_day = str()
    if current_hour >= 4 and current_hour <= 11:
        time_of_day = 'morning'
    elif current_hour >= 12 and current_hour <= 16:
        time_of_day = 'afternoon'
    else:
        time_of_day = 'evening'
    
    context = {
        'cards': [  
            create_contact_info_card(
                'Email',
                'cahu@umich.edu',
                f'mailto:cahu@umich.edu?subject=Hello from the Website!&body=Good {time_of_day}, Cam!%0D%0A%0D%0A<YOUR MESSAGE HERE>%0D%0A%0D%0ABest,%0D%0A<YOUR NAME>',
                '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 18"><path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2zm13 2.383-4.758 2.855L15 11.114v-5.73zm-.034 6.878L9.271 8.82 8 9.583 6.728 8.82l-5.694 3.44A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.739zM1 11.114l4.758-2.876L1 5.383v5.73z"/></svg>'
            ),
            create_contact_info_card(
                'Phone',
                '+1 (248) 425-5199',
                'tel:+1 (248) 425-5199',
                '<svg id="svg-1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-telephone" viewBox="0 0 16 18"><path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/></svg>'
            ),
            create_contact_info_card(
                'Anonymous Message',
                'Send Cam a message anonymously!',
                '/anonymous-message',
                '<svg version="1.0" xmlns="http://www.w3.org/2000/svg"  width="32" height="32" viewBox="0 0 340 340"  preserveAspectRatio="xMidYMid meet"><g transform="translate(-60,370) scale(0.14,-0.14)" fill="currentColor" stroke="none"><path d="M1242 2634 c-66 -33 -138 -112 -186 -204 -21 -40 -64 -151 -96 -248 l-57 -175 -74 -27 c-222 -81 -332 -183 -333 -309 0 -110 70 -194 226 -269 78 -38 99 -53 107 -76 6 -16 11 -30 11 -31 0 -1 -26 -19 -57 -40 -76 -50 -212 -182 -275 -268 -50 -67 -51 -69 -32 -87 10 -10 97 -70 192 -135 94 -64 172 -121 172 -126 0 -5 -27 -63 -60 -129 l-60 -120 910 0 c500 0 910 2 910 5 0 3 -27 59 -60 125 -33 66 -60 121 -60 124 0 2 19 16 43 31 23 15 111 75 195 132 l152 104 -41 61 c-56 82 -165 195 -240 249 -104 74 -101 72 -94 102 6 22 24 35 100 72 51 25 115 65 141 88 85 75 115 184 75 272 -38 85 -180 184 -334 232 -53 17 -58 21 -68 58 -58 213 -153 431 -224 512 -88 101 -174 122 -340 83 -107 -25 -186 -25 -295 0 -120 27 -184 26 -248 -6z m233 -188 c95 -21 222 -20 325 4 145 33 160 28 228 -85 43 -72 162 -428 162 -486 0 -48 -275 -75 -670 -65 -254 6 -344 16 -410 42 -47 19 -48 13 17 224 54 175 107 292 159 350 43 47 46 48 189 16z m-559 -681 c15 -20 46 -47 68 -60 107 -63 390 -92 798 -81 350 8 497 44 565 135 14 20 28 38 29 40 5 6 138 -59 171 -85 18 -14 33 -33 33 -44 0 -48 -147 -126 -326 -171 -510 -129 -1323 -63 -1530 124 l-46 42 27 33 c22 26 150 100 177 102 4 0 19 -16 34 -35z m290 -495 c16 0 26 -11 38 -45 48 -124 214 -165 305 -75 16 17 32 43 36 60 6 28 10 30 50 30 41 0 43 -2 49 -34 12 -64 101 -114 180 -102 69 12 121 49 151 110 24 50 29 54 68 59 23 3 43 5 44 4 6 -7 -32 -161 -54 -217 -64 -159 -177 -296 -292 -353 -56 -28 -75 -32 -141 -31 -126 1 -222 52 -321 171 -77 93 -157 269 -175 388 -7 47 -6 48 17 42 13 -4 34 -7 45 -7z m1183 -188 c64 -52 146 -131 141 -135 -3 -3 -79 -55 -170 -117 -91 -62 -169 -116 -173 -120 -5 -4 3 -30 17 -58 14 -28 26 -56 26 -62 0 -6 -50 -10 -140 -10 l-141 0 67 62 c128 120 210 265 264 466 l11 44 27 -18 c15 -9 47 -33 71 -52z m-1381 -45 c48 -153 109 -254 219 -364 l91 -93 -143 0 -144 0 28 62 28 63 -166 113 c-91 63 -170 118 -176 123 -5 6 8 27 35 55 50 51 169 144 185 144 6 0 25 -46 43 -103z"/></g></svg>'
            ),
            create_contact_info_card(
                'Add Contact',
                'Put Cam in your contacts!',
                '/static/files/cam-hudson.vcard" target="_blank',
                '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-person-plus" viewBox="0 0 16 18"><path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H1s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C9.516 10.68 8.289 10 6 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/><path fill-rule="evenodd" d="M13.5 5a.5.5 0 0 1 .5.5V7h1.5a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0V8h-1.5a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5z"/></svg>'
            ),
            create_contact_info_card(
                'Report a Bug',
                'Tell Cam about a website bug!',
                '/bug',
                '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-bug" viewBox="0 0 16 18"><path d="M4.355.522a.5.5 0 0 1 .623.333l.291.956A4.979 4.979 0 0 1 8 1c1.007 0 1.946.298 2.731.811l.29-.956a.5.5 0 1 1 .957.29l-.41 1.352A4.985 4.985 0 0 1 13 6h.5a.5.5 0 0 0 .5-.5V5a.5.5 0 0 1 1 0v.5A1.5 1.5 0 0 1 13.5 7H13v1h1.5a.5.5 0 0 1 0 1H13v1h.5a1.5 1.5 0 0 1 1.5 1.5v.5a.5.5 0 1 1-1 0v-.5a.5.5 0 0 0-.5-.5H13a5 5 0 0 1-10 0h-.5a.5.5 0 0 0-.5.5v.5a.5.5 0 1 1-1 0v-.5A1.5 1.5 0 0 1 2.5 10H3V9H1.5a.5.5 0 0 1 0-1H3V7h-.5A1.5 1.5 0 0 1 1 5.5V5a.5.5 0 0 1 1 0v.5a.5.5 0 0 0 .5.5H3c0-1.364.547-2.601 1.432-3.503l-.41-1.352a.5.5 0 0 1 .333-.623zM4 7v4a4 4 0 0 0 3.5 3.97V7H4zm4.5 0v7.97A4 4 0 0 0 12 11V7H8.5zM12 6a3.989 3.989 0 0 0-1.334-2.982A3.983 3.983 0 0 0 8 2a3.983 3.983 0 0 0-2.667 1.018A3.989 3.989 0 0 0 4 6h8z"/></svg>'
            )
        ]
    }
    return render_template('contact-info.html', **context)
