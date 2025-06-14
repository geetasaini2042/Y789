from flask import Flask, Response, request
import requests

app = Flask(__name__)

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
    "/cloudflare/ads-images/":"https://sainipankaj12.serv00.net/TelegramStream.php?file_id=AgACAgUAAyEGAASQTtqMAAJL1mhNbj_k7-DVAAH8jtdND-LL19ylswACA8UxG1bUaFZdU24p1KlgsAAIAQADAgADeQAHHgQ&file_type=photo&",
    "/cdn-cgi/scripts/7d0fa10a/cloudflare-static/rocket-loader.min.js":"https://geetasaini2042.github.io/17uio/Data/App/cdn-cgi/scripts/7d0fa10a/cloudflare-static/rocket-loader.min.js",
    "/get-fresh-csrf-token":"https://getmodsapk.com/get-fresh-csrf-token",
    "/track-view/":"https://getmodsapk.com/track-view/",
    "my_download": "https://getmodsapk.com/dl-track/",
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
