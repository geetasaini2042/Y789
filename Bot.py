from flask import Flask, Response, request
import requests

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins



# Replace list: key = original text, value = replacement text
replace_list1 = {
    "https://9mod.com/wp-content/uploads/2024/06/number-9-small.png": "https://geetasaini2042.github.io/17uio/Data/App2/wp-content/uploads/2024/06/number-9-small.png",
    '<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">':"""
     <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
     <script src="https://telegram.org/js/telegram-web-app.js"></script>
     <script src='//libtl.com/sdk.js' data-zone='9429528' data-sdk='show_9429528'></script>
""",
    "https://9mod.com/wp-includes/": "https://geetasaini2042.github.io/17uio/Data/App2/wp-includes/",
    "https://9mod.com/wp-content/themes/9mod/": "https://geetasaini2042.github.io/17uio/Data/App2/wp-content/themes/9mod/",
    "https://9mod.com/": "/server2/",
    "https://9mod.com" : "/server2",
    "9MOD.COM" :  "PREMIUM HUB",
    "/?s" : "/server2/",
    "/server2/cloudflare/ads-images/":"https://sainipankaj12.serv00.net/TelegramStream.php?file_id=AgACAgUAAyEGAASQTtqMAAJL1mhNbj_k7-DVAAH8jtdND-LL19ylswACA8UxG1bUaFZdU24p1KlgsAAIAQADAgADeQAHHgQ&file_type=photo&",
    "/cdn-cgi/challenge-platform/":"/server2/cdn-cgi/challenge-platform/",
    "/server2/cdn-cgi/challenge-platform/h/b/jsd/":"https://sainipankaj12.serv00.net/App/Pre/getmod.php/cdn-cgi/challenge-platform/h/b/jsd/",
    '/server2/wp-content/uploads/': 'https://9mod.com/wp-content/uploads/',
    '/server2/tips/': 'https://geetasaini2042.github.io/17uio/Data/App2/tips/',
    '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8513869610548047"':"",
    'crossorigin="anonymous"></script>':"",
    'class="adsbygoogle"':"",
     'style="display:block"':"",
     'data-ad-client="ca-pub-8513869610548047"':"",
     'data-ad-slot="7007044823"':"",
     'data-ad-format="auto"':"",
     'data-full-width-responsive="true"':"",
     '(adsbygoogle = window.adsbygoogle || []).push({});':"",
     '<ins' :"",
     '></ins>':"""<div style="width:100%; text-align:center; margin:10px 0;">
  <a href="https://otieu.com/4/9111282" target="_blank" rel="noopener noreferrer">
    <img src="https://geetasaini2042.github.io/17uio/Data/App/cloudflare/ads-images/PREMIUM%20HUB-ADS5.png" 
         alt="Advertisement" 
         style="max-width:100%; height:auto; border-radius:12px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
  </a>
</div>""",
    """</body>""":"""
    <script>
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".download-button").forEach(button => {
  const originalEncoded = button.getAttribute("data-href");
  let decodedUrl = atob(originalEncoded);

  // /1 जोड़ना सुनिश्चित करें
  if (!decodedUrl.endsWith("/1")) {
    if (decodedUrl.endsWith("/")) {
      decodedUrl += "1";
    } else {
      decodedUrl += "/1";
    }
  }

  // Premium HUB iframe URL बनाएँ
  const iframeUrl = "https://geetasaini2042.github.io/17uio/APPS/Ifram.html?url=" + encodeURIComponent(decodedUrl);

  // फिर से encode करें
  const newEncoded = btoa(iframeUrl);
  button.setAttribute("data-href", newEncoded);
});

// Click पर Telegram Mini App में open करें
document.querySelectorAll(".download-button").forEach(button => {
  button.addEventListener("click", function (e) {
    e.preventDefault();

    show_9429528().then(() => {
      const decoded = atob(this.getAttribute("data-href"));

      // ✅ Mini App के अंदर URL खोलें
      if (window.Telegram && Telegram.WebApp) {
        Telegram.WebApp.openLink(decoded); // Telegram Mini App में खोलने के लिए
      } else {
        // fallback — अगर बाहर है
        window.location.href = decoded;
      }

    }).catch(err => {
      console.error("Ad failed or skipped:", err);
    });
  });
});
});
</script></body>"""
}

@app.route('/server2/', defaults={'path': ''}, methods=['GET', 'POST', 'OPTIONS'])
@app.route('/server2/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
def proxy12(path):
    target_url = f"https://9mod.com/{path}"

    # Forward query parameters
    if request.query_string:
        target_url += '?' + request.query_string.decode()

    try:
        # Handle preflight CORS request
        if request.method == 'OPTIONS':
            response = Response()
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
            return response

        # Choose request method
        if request.method == 'GET':
            upstream_response = requests.get(target_url, headers={
                "User-Agent": request.headers.get('User-Agent', 'Mozilla/5.0')
            })

        elif request.method == 'POST':
            upstream_response = requests.post(target_url,
                headers={"Content-Type": request.headers.get("Content-Type", "application/json")},
                data=request.get_data()
            )

        else:
            return Response("Method not allowed", status=405)

        content = upstream_response.text

        # Text-based content replace (e.g., HTML/JS/CSS)
        if 'text' in upstream_response.headers.get('Content-Type', '') or 'application/javascript' in upstream_response.headers.get('Content-Type', ''):
            for original, replacement in replace_list1.items():
                content = content.replace(original, replacement)

            response = Response(content, status=upstream_response.status_code)
        else:
            # Binary files or others
            response = Response(upstream_response.content, status=upstream_response.status_code)

        # Set content type and CORS
        response.headers['Content-Type'] = upstream_response.headers.get('Content-Type', 'text/html')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)


# Replace list: key = original text, value = replacement text
replace_list = {
    "https://getmodsapk.com/storage/media/2025/4/favicon/": "https://geetasaini2042.github.io/17uio/Data/App/storage/media/2025/4/favicon/",
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">':"""
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <script src='//libtl.com/sdk.js' data-zone='9429528' data-sdk='show_9429528'></script>
""",
    "https://getmodsapk.com/build/": "https://geetasaini2042.github.io/17uio/Data/App/build/",
    "https://getmodsapk.com/storage/media/2025/4/logo/": "https://geetasaini2042.github.io/17uio/Data/App/storage/media/2025/4/logo/",
    "https://getmodsapk.com/images/": "https://geetasaini2042.github.io/17uio/Data/App/images/",
    "https://t.me/GETMODSAPK_COM": "https://t.me/aibots72",
    "https://t.me/GETMODSAPKCOM": "https://t.me/mr_singodiyabot",
    "https://whatsapp.com/channel/0029Vb6IyLyCnA7lVY6SMi44": "https://whatsapp.com/channel/0029Vb6GLU7AjPXQozg6Fv3S",
    "https://getmodsapk.com/dl-track/": "my_download",
    "https://getmodsapk.com/": "/",
    "https://getmodsapk.com":"/",
    "GETMODAPK.COM":"TECH HUB",
    "GETMODSAPK.COM":"PREMIUM HUB",
    "GetModsApk":"PREMIUM HUB",
    "/cloudflare/ads-images/":"https://sainipankaj12.serv00.net/TelegramStream.php?file_id=AgACAgUAAyEGAASQTtqMAAJL12hNgeAmhYqUhToB5bKBEn8veCtuAAL9xjEbVtRwVmozxoD3eEdPAAgBAAMCAAN5AAceBA&file_type=photo&",
    "/cdn-cgi/scripts/7d0fa10a/cloudflare-static/rocket-loader.min.js":"https://geetasaini2042.github.io/17uio/Data/App/cdn-cgi/scripts/7d0fa10a/cloudflare-static/rocket-loader.min.js",
    "/get-fresh-csrf-token":"https://getmodsapk.com/get-fresh-csrf-token",
    "/track-view/":"https://getmodsapk.com/track-view/",
    "my_download": "https://geetasaini2042.github.io/17uio/Data/index.html?url=https://getmodsapk.com/dl-track/",
    'src="/storage/': 'src="https://getmodsapk.com/storage/',
    'src="/uploads/': 'src="https://geetasaini2042.github.io/17uio/Data/App/uploads/',
    '"thumbnailUrl":"/storage/': '"thumbnailUrl":"https://getmodsapk.com/storage/',
    'src="../../../storage/': 'src="https://getmodsapk.com/storage/',
    "https://so-gr3at3.com/go/1236791":"https://otieu.com/4/9448242",
    """document.addEventListener('DOMContentLoaded', function() {
        const download_links = document.querySelectorAll('.download-links');
        download_links.forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();

                const randomNumber = Math.random();
                let targetUrl = 'https://otieu.com/4/9448242'; // Default URL

                // Logic seems redundant as it always assigns the same URL
                // if (randomNumber < 1) { // This is always true
                //     targetUrl = 'https://otieu.com/4/9448242';
                // } else {
                //     targetUrl = 'https://otieu.com/4/9448242';
                // }

                window.open(targetUrl, '_blank');

                let downloadLink = e.target.closest('a');
                if (downloadLink && downloadLink.href) {
                     window.location.href = downloadLink.href;
                }
            });
        });
    });""":"""document.addEventListener('DOMContentLoaded', function () {
        const download_links = document.querySelectorAll('.download-links');

        download_links.forEach(item => {
            item.addEventListener('click', function (e) {
                e.preventDefault();

                const downloadLink = e.target.closest('a');

                if (!downloadLink || !downloadLink.href) {
                    console.error("Download link not found!");
                    return;
                }

                // Ad show using libtl SDK
                if (typeof show_9429528 === 'function') {
                    show_9429528().then(() => {
                        // Ad shown successfully, now start download
                        window.location.href = downloadLink.href;
                    }).catch(err => {
                        console.error("Ad display failed:", err);
                        // If ad fails, fallback to direct download
                        window.location.href = downloadLink.href;
                    });
                } else {
                    console.warn("Ad function show_9429528 not available!");
                    window.location.href = downloadLink.href;
                }
            });
        });
    });"""
}
@app.route('/api/hello')
def api_hello():
    return 'This Is Premium app bot running at clubofupsc@gmail.com'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    target_url = f"https://getmodsapk.com/{path}"

    # Forward user query parameters
    if request.query_string:
        target_url += '?' + request.query_string.decode()

    try:
        # Fetch original content
        response = requests.get(target_url, headers={
            "User-Agent": request.headers.get('User-Agent', 'Mozilla/5.0')
        })

        if response.status_code != 200:
            return f"Error fetching: {target_url}", response.status_code

        content = response.text

        # Apply replacements
        for original, replacement in replace_list.items():
            content = content.replace(original, replacement)

        # Return modified HTML
        return Response(content, content_type=response.headers.get('Content-Type', 'text/html'))

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
