import base64

openFile = "output.txt"

with open(openFile, "r") as file:
    file_content = file.read()

lines = file_content.split("split")


html_content_p1 = """ <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Professional Email</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        text-align: center;
        background-color: #f9f9f9;
      }
      .header {
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #dddddd;
        padding: 20px;
        background-color: #222831;
        color: whitesmoke;
      }
      .header img {
        max-width: 30px;
        margin-right: 20px;
        height: auto;
      }
      .container {
        margin: 0 auto;
        max-width: 600px;
        display: flex;
        flex-direction: column;
        gap: 0;
      }

      .box {
        border: 1px solid #dddddd;
      }

      header,
      .content {
        padding: 30px;
        text-align: left;
        background-color: #f9f9f9;
      }
      .colors {
        color: darkblue;
      }
      footer {
        padding: 30px;
        text-align: left;
        background-color: #222831;
      }

      header h1,
      footer p {
        margin: 0;
        font-size: 16px;
        color: #333;
      }

      p {
        font-size: 12px;
        color: #333;
        margin-bottom: 10px;
      }
      .social-media {
        display: flex;
        justify-content: center;
        margin-top: 20px;
      }

      .social-media a {
        margin: 0 10px;
      }

      .social-media img {
        width: 30px;
        height: auto;
      }

      .section-with-image {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
      }

      .section-with-image img {
        max-width: 150px;
        height: auto;
        margin-right: 50px;
      }

      .section-with-image h5 {
        margin: 0;
        font-size: 16px;
        color: #333;
      }

      .section-with-image-right {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
      }

      .section-with-image-right img {
        max-width: 150px;
        height: auto;
        margin-left: 50px;
      }

      .section-with-image-right h5 {
        margin: 0;
        font-size: 16px;
        color: #333;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <img src="./img/Logo.png" alt="Newsletter Logo" />
        <h3>SkyHigh Insights</h3>
      </div>

      <div class="box">
        <div class="content">
          <div class="section-with-image">
            <img src="./img/flight.png" alt="Image" />
            <div>
            """
html_content_p2 = f"""
      
              <h5 class="colors">
                Company Flights and Stock Information:
              </h5>

              <p>
                {
                    "".join(lines[2])
                }

              </p>
            </div>
          </div>
          <div
            class="section-with-image-right"
            style="flex-direction: row-reverse"
          >
            <img src="./img/stock-market.png" alt="Image" />
            <!--
              <a href="https://www.flaticon.com/free-icons/stock-market" title="stock market icons">Stock market icons created by Freepik - Flaticon</a>
            -->
            <div>
              <h5 class="colors">Weekly Market Overview</h5>
              <p>
                {
                    "".join(lines[3])
                }
              </p>
            </div>
          </div>
          <div class="section-with-image">
            <img src="./img/statistics.png" alt="Image" />
            <div>
              <h5 class="colors">Conclusion</h5>
              <p>
                {
                    "".join(lines[4])
                }
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="box">
        <footer>
          <div class="social-media">
            <a href="#"><img src="./img/facebook-icon.png" alt="Facebook" /></a>
            <a href="#"><img src="./img/twitter-icon.png" alt="Twitter" /></a>
            <a href="#"><img src="./img/linkedin-icon.png" alt="LinkedIn" /></a>
            <a href="#"
              ><img src="./img/instagram-icon.png" alt="Instagram"
            /></a>  
          </div>
        </footer>
      </div>
    </div>
  </body>
</html>
"""
html_content = html_content_p1 + html_content_p2
base64encoded = "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CiAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCIgLz4KICAgIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsIGluaXRpYWwtc2NhbGU9MS4wIiAvPgogICAgPHRpdGxlPlByb2Zlc3Npb25hbCBFbWFpbDwvdGl0bGU+CiAgICA8c3R5bGU+CiAgICAgIGJvZHkgewogICAgICAgIG1hcmdpbjogMDsKICAgICAgICBwYWRkaW5nOiAwOwogICAgICAgIGZvbnQtZmFtaWx5OiBBcmlhbCwgc2Fucy1zZXJpZjsKICAgICAgICB0ZXh0LWFsaWduOiBjZW50ZXI7CiAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogI2Y5ZjlmOTsKICAgICAgfQogICAgICAuaGVhZGVyIHsKICAgICAgICBkaXNwbGF5OiBmbGV4OwogICAgICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgICAgICAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7CiAgICAgICAgYm9yZGVyOiAxcHggc29saWQgI2RkZGRkZDsKICAgICAgICBwYWRkaW5nOiAyMHB4OwogICAgICAgIGJhY2tncm91bmQtY29sb3I6ICMyMjI4MzE7CiAgICAgICAgY29sb3I6IHdoaXRlc21va2U7CiAgICAgIH0KICAgICAgLmhlYWRlciBpbWcgewogICAgICAgIG1heC13aWR0aDogMzBweDsKICAgICAgICBtYXJnaW4tcmlnaHQ6IDIwcHg7CiAgICAgICAgaGVpZ2h0OiBhdXRvOwogICAgICB9CiAgICAgIC5jb250YWluZXIgewogICAgICAgIG1hcmdpbjogMCBhdXRvOwogICAgICAgIG1heC13aWR0aDogNjAwcHg7CiAgICAgICAgZGlzcGxheTogZmxleDsKICAgICAgICBmbGV4LWRpcmVjdGlvbjogY29sdW1uOwogICAgICAgIGdhcDogMDsKICAgICAgfQogICAgICAuYm94IHsKICAgICAgICBib3JkZXI6IDFweCBzb2xpZCAjZGRkZGRkOwogICAgICB9CiAgICAgIGhlYWRlciwKICAgICAgLmNvbnRlbnQgewogICAgICAgIHBhZGRpbmc6IDMwcHg7CiAgICAgICAgdGV4dC1hbGlnbjogbGVmdDsKICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjZjlmOWY5OwogICAgICB9CiAgICAgIC5jb2xvcnMgewogICAgICAgIGNvbG9yOiBkYXJrYmx1ZTsKICAgICAgfQogICAgICBmb290ZXIgewogICAgICAgIHBhZGRpbmc6IDMwcHg7CiAgICAgICAgdGV4dC1hbGlnbjogbGVmdDsKICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjMjIyODMxOwogICAgICB9CiAgICAgIGhlYWRlciBoMSwKICAgICAgZm9vdGVyIHAgewogICAgICAgIG1hcmdpbjogMDsKICAgICAgICBmb250LXNpemU6IDE2cHg7CiAgICAgICAgY29sb3I6ICMzMzM7CiAgICAgIH0KICAgICAgcCB7CiAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgIGNvbG9yOiAjMzMzOwogICAgICAgIG1hcmdpbi1ib3R0b206IDEwcHg7CiAgICAgIH0KICAgICAgLnNvY2lhbC1tZWRpYSB7CiAgICAgICAgZGlzcGxheTogZmxleDsKICAgICAgICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICAgICAgICBtYXJnaW4tdG9wOiAyMHB4OwogICAgICB9CiAgICAgIC5zb2NpYWwtbWVkaWEgYSB7CiAgICAgICAgbWFyZ2luOiAwIDEwcHg7CiAgICAgIH0KICAgICAgLnNvY2lhbC1tZWRpYSBpbWcgewogICAgICAgIHdpZHRoOiAzMHB4OwogICAgICAgIGhlaWdodDogYXV0bzsKICAgICAgfQogICAgICAuc2VjdGlvbi13aXRoLWltYWdlIHsKICAgICAgICBkaXNwbGF5OiBmbGV4OwogICAgICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgICAgICAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7CiAgICAgICAgbWFyZ2luLWJvdHRvbTogMjBweDsKICAgICAgfQogICAgICAuc2VjdGlvbi13aXRoLWltYWdlIGltZyB7CiAgICAgICAgbWF4LXdpZHRoOiAxNTBweDsKICAgICAgICBoZWlnaHQ6IGF1dG87CiAgICAgICAgbWFyZ2luLXJpZ2h0OiA1MHB4OwogICAgICB9CiAgICAgIC5zZWN0aW9uLXdpdGgtaW1hZ2UgaDUgewogICAgICAgIG1hcmdpbjogMDsKICAgICAgICBmb250LXNpemU6IDE2cHg7CiAgICAgICAgY29sb3I6ICMzMzM7CiAgICAgIH0KICAgICAgLnNlY3Rpb24td2l0aC1pbWFnZS1yaWdodCB7CiAgICAgICAgZGlzcGxheTogZmxleDsKICAgICAgICBhbGlnbi1pdGVtczogY2VudGVyOwogICAgICAgIGp1c3RpZnktY29udGVudDogY2VudGVyOwogICAgICAgIG1hcmdpbi1ib3R0b206IDIwcHg7CiAgICAgIH0KICAgICAgLnNlY3Rpb24td2l0aC1pbWFnZS1yaWdodCBpbWcgewogICAgICAgIG1heC13aWR0aDogMTUwcHg7CiAgICAgICAgaGVpZ2h0OiBhdXRvOwogICAgICAgIG1hcmdpbi1sZWZ0OiA1MHB4OwogICAgICB9CiAgICAgIC5zZWN0aW9uLXdpdGgtaW1hZ2UtcmlnaHQgaDUgewogICAgICAgIG1hcmdpbjogMDsKICAgICAgICBmb250LXNpemU6IDE2cHg7CiAgICAgICAgY29sb3I6ICMzMzM7CiAgICAgIH0KICAgIDwvc3R5bGU+CiAgPC9oZWFkPgogIDxib2R5PgogICAgPGRpdiBjbGFzcz0iY29udGFpbmVyIj4KICAgICAgPGRpdiBjbGFzcz0iaGVhZGVyIj4KICAgICAgICA8aW1nIHNyYz0iLi9pbWcvTG9nby5wbmciIGFsdD0iTmV3c2xldHRlciBMb2dvIiAvPgogICAgICAgIDxoMz5Ta3lIaWdoIEluc2lnaHRzPC9oMz4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImJveCI+CiAgICAgICAgPGRpdiBjbGFzcz0iY29udGVudCI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzZWN0aW9uLXdpdGgtaW1hZ2UiPgogICAgICAgICAgICA8aW1nIHNyYz0iLi9pbWcvZmxpZ2h0LnBuZyIgYWx0PSJJbWFnZSIgLz4KICAgICAgICAgICAgPGRpdj4KICAgICAgICAgICAgCiAgICAgICAgICAgICAgPGg1IGNsYXNzPSJjb2xvcnMiPkNvbXBhbnkgRmxpZ2h0cyBhbmQgU3RvY2sgSW5mb3JtYXRpb246PC9oNT4KICAgICAgICAgICAgICA8cD4KVGhpcyB3ZWVrLCB3ZSB3aWxsIGJlIGZvY3VzaW5nIG9uIHRoZSBmbGlnaHQgZGV0YWlscyBhbmQgc3RvY2sgcGVyZm9ybWFuY2Ugb2YgdGhyZWUgY29tcGFuaWVzOiA8Yj5HTFc8L2I+LCA8Yj5IRDwvYj4sIGFuZCA8Yj5BQkM8L2I+LiBMZXQncyB0YWtlIGEgY2xvc2VyIGxvb2sgYXQgdGhlaXIgcmVjZW50IGZsaWdodHMgYW5kIHN0b2NrIGluZm9ybWF0aW9uLgoKRmxpZ2h0IERldGFpbHM6Ci0gPGI+R0xXPC9iPjogRnJvbSA8Yj5Nb3JyaXN0b3duPC9iPiB0byA8Yj5DbGVhciBXYXRlcjwvYj4uCi0gPGI+SEQ8L2I+OiBGcm9tIDxiPlNwb2thbmU8L2I+IHRvIDxiPlNhY3JhbWVudG88L2I+LgotIDxiPkFCQzwvYj46IEZyb20gPGI+Q2l0eSBYPC9iPiB0byA8Yj5DaXR5IFk8L2I+LgoKU3RvY2sgUGVyZm9ybWFuY2U6Ci0gU3RvY2sgSW5mb3JtYXRpb24gZm9yIEdMVzoKQ29tcGFueSBOYW1lOiBDb3JuaW5nIEluY29ycG9yYXRlZApQL0UgUmF0aW86IDE3LjA3ODk0NwpFUFM6IDAuNTEKQmV0YTogMS4wNDgKNTIgV2VlayBIaWdoOiA0Ni4zOQo1MiBXZWVrIExvdzogMjUuMjYKTWFya2V0IENhcDogMzMuMzIgYmlsbGlvbgpEaXZpZGVuZCBZaWVsZDogMi44OCUKUmV2ZW51ZTogMTIuMzkgYmlsbGlvbgpOZXQgSW5jb21lOiA0MzcgbWlsbGlvbgpQcmV2aW91cyBDbG9zZTogJDQwLjA0Ck9wZW46ICQzOS40NgpWb2x1bWU6IDUuNTMgbWlsbGlvbgpBdmVyYWdlIFZvbHVtZTogOC4yIG1pbGxpb24KCi0gU3RvY2sgSW5mb3JtYXRpb24gZm9yIEhEOgpDb21wYW55IE5hbWU6IEhvbWUgRGVwb3QsIEluYy4gKFRoZSkKUC9FIFJhdGlvOiAyMS42NzI1NjIKRVBTOiAxNC45MwpCZXRhOiAwLjk4OQo1MiBXZWVrIEhpZ2g6ICQzOTYuODcKNTIgV2VlayBMb3c6ICQyNzQuMjYKTWFya2V0IENhcDogMzUyLjQ1IGJpbGxpb24KRGl2aWRlbmQgWWllbGQ6IDIuNTMlClJldmVudWU6IDE1MS44MyBiaWxsaW9uCk5ldCBJbmNvbWU6IDE0Ljg3IGJpbGxpb24KUHJldmlvdXMgQ2xvc2U6ICQzNTguNTgKT3BlbjogJDM1NC45MwpWb2x1bWU6IDIuOTUgbWlsbGlvbgpBdmVyYWdlIFZvbHVtZTogMy40OSBtaWxsaW9uCgotIFN0b2NrIEluZm9ybWF0aW9uIGZvciBBQkM6CkNvbXBhbnkgTmFtZTogTi9BClAvRSBSYXRpbzogTi9BCkVQUzogTi9BCkJldGE6IE4vQQo1MiBXZWVrIEhpZ2g6IE4vQQo1MiBXZWVrIExvdzogTi9BCk1hcmtldCBDYXA6IE4vQQpEaXZpZGVuZCBZaWVsZDogTi9BClJldmVudWU6IE4vQQpOZXQgSW5jb21lOiBOL0EKUHJldmlvdXMgQ2xvc2U6IE4vQQpPcGVuOiBOL0EKVm9sdW1lOiBOL0EKQXZlcmFnZSBWb2x1bWU6IE4vQQoKR0xXLCBhbHNvIGtub3duIGFzIENvcm5pbmcgSW5jb3Jwb3JhdGVkLCBoYXMgaGFkIGEgc29saWQgd2VlayB3aXRoIGEgMi40JSBpbmNyZWFzZSBpbiBzdG9jayBwcmljZS4gVGhpcyBjYW4gYmUgYXR0cmlidXRlZCB0byB0aGVpciByZWNlbnQgZmxpZ2h0IGZyb20gTW9ycmlzdG93biB0byBDbGVhciBXYXRlciwgd2hpY2ggbWF5IGluZGljYXRlIGEgcG90ZW50aWFsIGV4cGFuc2lvbiBvciBhY3F1aXNpdGlvbiBpbiB0aGF0IGFyZWEuIEhELCBvciBIb21lIERlcG90LCBoYXMgYWxzbyBzZWVuIGEgMi41JSBpbmNyZWFzZSBpbiBzdG9jayBwcmljZSBhZnRlciB0aGVpciBmbGlnaHQgZnJvbSBTcG9rYW5lIHRvIFNhY3JhbWVudG8uIFRoaXMgY291bGQgc2lnbmFsIGEgbmV3IHN0b3JlIG9wZW5pbmcgb3Igb3RoZXIgc3RyYXRlZ2ljIG1vdmUgaW4gdGhhdCByZWdpb24uIFVuZm9ydHVuYXRlbHksIHdlIHdlcmUgdW5hYmxlIHRvIGdhdGhlciBhbnkgaW5mb3JtYXRpb24gb24gdGhlIGZsaWdodCBmb3IgQUJDLCBhcyB0aGUgY29tcGFueSBuYW1lIHdhcyBub3QgcHJvdmlkZWQuIEhvd2V2ZXIsIGl0IGlzIGltcG9ydGFudCB0byBub3RlIHRoYXQgdGhlaXIgc3RvY2sgaW5mb3JtYXRpb24gaXMgbm90IGF2YWlsYWJsZSwgd2hpY2ggY291bGQgaW5kaWNhdGUgYSBzbWFsbGVyIG9yIHByaXZhdGUgY29tcGFueS4KCjwvcD4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9InNlY3Rpb24td2l0aC1pbWFnZS1yaWdodCIgc3R5bGU9ImZsZXgtZGlyZWN0aW9uOiByb3ctcmV2ZXJzZSI+CiAgICAgICAgICAgIDxpbWcgc3JjPSIuL2ltZy9zdG9jay1tYXJrZXQucG5nIiBhbHQ9IkltYWdlIiAvPgogICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgIDxoNSBjbGFzcz0iY29sb3JzIj5XZWVrbHkgTWFya2V0IE92ZXJ2aWV3PC9oNT4KICAgICAgICAgICAgICA8cD4KIyMjIFdlZWtseSBNYXJrZXQgT3ZlcnZpZXcKCk1ham9yIEluZGljZXMgUGVyZm9ybWFuY2U6Ci0gXkdTUEM6IExhc3QgNSBkYXlzIGNsb3NlIHByaWNlczogNTQ2My41NCwgNTQzNi40NCwgNTUyMi4zLCA1NDQ2LjY4LCA1MzQ2LjU2Ci0gXkRKSTogTGFzdCA1IGRheXMgY2xvc2UgcHJpY2VzOiA0MDUzOS45MywgNDA3NDMuMzMsIDQwODQyLjc5LCA0MDM0Ny45NywgMzk3MzcuMjYKLSBeSVhJQzogTGFzdCA1IGRheXMgY2xvc2UgcHJpY2VzOiAxNzM3MC4yLCAxNzE0Ny40MiwgMTc1OTkuNCwgMTcxOTQuMTUsIDE2Nzc2LjE2CgpTZWN0b3IgUGVyZm9ybWFuY2U6Ci0gWExCOiBMYXN0IDUgZGF5cyBjbG9zZSBwcmljZXM6ICQ5MS40OSwgJDkxLjE5LCAkOTIuMTQsICQ5MS43NywgJDkwLjA0Ci0gWExDOiBMYXN0IDUgZGF5cyBjbG9zZSBwcmljZXM6ICQ4NC40NCwgJDg0Ljc4LCAkODUuNzksICQ4Ni4xNCwgJDg0Ljc0Ci0gWExEOiBMYXN0IDUgZGF5cyBjbG9zZSBwcmljZXM6IAotIFhMRTogTGFzdCA1IGRheXMgY2xvc2UgcHJpY2VzOiAkOTEuNCwgJDkyLjgyLCAkOTMuMjEsICQ5MC43NCwgJDg4LjQKLSBYTEY6IExhc3QgNSBkYXlzIGNsb3NlIHByaWNlczogJDQzLjM1LCAkNDMuODUsICQ0My43NCwgJDQzLjEyLCAkNDIuMDYKLSBYTEk6IExhc3QgNSBkYXlzIGNsb3NlIHByaWNlczogJDEyNi4wOCwgJDEyNi40NSwgJDEyNy44NiwgJDEyNS40OSwgJDEyMi43MwotIFhMUDogTGFzdCA1IGRheXMgY2xvc2UgcHJpY2VzOiAkNzguNTIsICQ3Ny45OSwgJDc3Ljg1LCAkNzguNTcsICQ3OS4yNgotIFhMVTogTGFzdCA1IGRheXMgY2xvc2UgcHJpY2VzOiAkNzEuNDksICQ3MS44NiwgJDcyLjc5LCAkNzQuMSwgJDc0LjIyCi0gWExZOiBMYXN0IDUgZGF5cyBjbG9zZSBwcmljZXM6ICQxODUuNjYsICQxODQuNjMsICQxODcuNDksICQxODIuODksICQxNzYuMTYKClRoaXMgd2VlaywgdGhlIG1hcmtldCBoYXMgc2VlbiBtaXhlZCBwZXJmb3JtYW5jZSB3aXRoIHRoZSBTJlAgNTAwIGFuZCBEb3cgSm9uZXMgc2xpZ2h0bHkgZG93biwgd2hpbGUgdGhlIE5BU0RBUSBoYXMgcmVtYWluZWQgcmVsYXRpdmVseSBzdGFibGUuIFRoZSBpbmR1c3RyaWFsIHNlY3RvciAoWExJKSBoYXMgc2VlbiB0aGUgYmlnZ2VzdCBkZWNsaW5lLCB3aGlsZSB0aGUgZW5lcmd5IHNlY3RvciAoWExFKSBoYXMgc2VlbiB0aGUgYmlnZ2VzdCBnYWlucy4gVGhpcyBjb3VsZCBiZSBkdWUgdG8gdGhlIHJlY2VudCByaXNlIGluIG9pbCBwcmljZXMuIE92ZXJhbGwsIHRoZSBtYXJrZXQgaGFzIGJlZW4gaW5mbHVlbmNlZCBieSBlY29ub21pYyBpbmRpY2F0b3JzIHN1Y2ggYXMgaW5mbGF0aW9uIGFuZCBqb2IgZ3Jvd3RoLCBhcyB3ZWxsIGFzIG9uZ29pbmcgdHJhZGUgdGVuc2lvbnMuCgo8L3A+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzZWN0aW9uLXdpdGgtaW1hZ2UiPgogICAgICAgICAgICA8aW1nIHNyYz0iLi9pbWcvc3RhdGlzdGljcy5wbmciIGFsdD0iSW1hZ2UiIC8+CiAgICAgICAgICAgIDxkaXY+CiAgICAgICAgICAgICAgPGg1IGNsYXNzPSJjb2xvcnMiPkNvbmNsdXNpb248L2g1PgogICAgICAgICAgICAgIDxwPgpBcyB3ZSBsb29rIGFoZWFkLCBpdCBpcyBpbXBvcnRhbnQgZm9yIGludmVzdG9ycyB0byBrZWVwIGFuIGV5ZSBvbiBlY29ub21pYyBpbmRpY2F0b3JzIGFuZCBtYXJrZXQgdHJlbmRzLiBXaXRoIHBvdGVudGlhbCBtZXJnZXJzLCBhY3F1aXNpdGlvbnMsIGFuZCBleHBhbnNpb25zIG9uIHRoZSBob3Jpem9uIGZvciBjb21wYW5pZXMgbGlrZSBHTFcgYW5kIEhELCB0aGVyZSBtYXkgYmUgb3Bwb3J0dW5pdGllcyBmb3IgZ3Jvd3RoLiBIb3dldmVyLCBpdCBpcyBhbHNvIGltcG9ydGFudCB0byBiZSBjYXV0aW91cyBhbmQgY29uc2lkZXIgcG90ZW50aWFsIHJpc2tzIGluIHRoZSBtYXJrZXQuIFdlIGhvcGUgdGhpcyB3ZWVrJ3MgaW5zaWdodHMgaGF2ZSBwcm92aWRlZCB2YWx1YWJsZSBpbmZvcm1hdGlvbiBmb3IgaW52ZXN0b3JzIGFuZCB3ZSBsb29rIGZvcndhcmQgdG8gYnJpbmdpbmcgeW91IG1vcmUgaW4gdGhlIGZ1dHVyZS48L3A+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJib3giPgogICAgICAgIDxmb290ZXI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzb2NpYWwtbWVkaWEiPgogICAgICAgICAgICA8YSBocmVmPSIjIj48aW1nIHNyYz0iLi9pbWcvZmFjZWJvb2staWNvbi5wbmciIGFsdD0iRmFjZWJvb2siIC8+PC9hPgogICAgICAgICAgICA8YSBocmVmPSIjIj48aW1nIHNyYz0iLi9pbWcvdHdpdHRlci1pY29uLnBuZyIgYWx0PSJUd2l0dGVyIiAvPjwvYT4KICAgICAgICAgICAgPGEgaHJlZj0iIyI+PGltZyBzcmM9Ii4vaW1nL2xpbmtlZGluLWljb24ucG5nIiBhbHQ9IkxpbmtlZEluIiAvPjwvYT4KICAgICAgICAgICAgPGEgaHJlZj0iIyI+PGltZyBzcmM9Ii4vaW1nL2luc3RhZ3JhbS1pY29uLnBuZyIgYWx0PSJJbnN0YWdyYW0iIC8+PC9hPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9mb290ZXI+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgPC9ib2R5Pgo8L2h0bWw+Cg=="

decoded_html_content = base64.b64decode(base64encoded).decode('utf-8')
print(decoded_html_content)
file_name = "sample.html"
with open(file_name, "w") as file:
    file.write(html_content)


