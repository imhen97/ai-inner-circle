# -*- coding: utf-8 -*-
"""Regenerate apply.html (UTF-8). Run: python3 scripts/write_apply_html.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "apply.html"

CSS = r"""
  :root {
    --black: #080808;
    --off-white: #f0ece4;
    --gold: #c9a96e;
    --gold-light: #e8d5b0;
    --gold-dark: #8a6f3e;
    --grey-light: #8a8a8a;
    --border: rgba(201, 169, 110, 0.35);
    --surface: #121212;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
    font-weight: 400;
    background: var(--black);
    color: var(--off-white);
    line-height: 1.55;
    min-height: 100vh;
    padding: 1.5rem 1.25rem 3rem;
  }
  .wrap { max-width: 520px; margin: 0 auto; }
  .back {
    display: inline-block;
    font-size: 0.85rem;
    color: var(--gold);
    text-decoration: none;
    margin-bottom: 1.5rem;
    font-weight: 500;
  }
  .back:hover { text-decoration: underline; }
  .head-badge {
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.5rem;
  }
  h1 {
    font-size: 1.45rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    line-height: 1.35;
  }
  .lead {
    font-size: 0.95rem;
    color: var(--grey-light);
    margin-bottom: 2rem;
  }
  hr.sep {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.75rem 0;
  }
  .block-title {
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: var(--gold-light);
    margin-bottom: 1rem;
  }
  .hint {
    font-size: 0.8rem;
    color: var(--grey-light);
    margin-top: 0.35rem;
  }
  .field-label {
    display: block;
    font-size: 0.88rem;
    font-weight: 600;
    margin-bottom: 0.45rem;
    color: var(--off-white);
  }
  .req { color: var(--gold); font-weight: 700; }
  input[type="text"],
  input[type="tel"],
  input[type="email"],
  textarea {
    width: 100%;
    padding: 0.75rem 0.85rem;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--surface);
    color: var(--off-white);
    font-size: 1rem;
    font-family: inherit;
  }
  input:focus, textarea:focus {
    outline: 2px solid var(--gold);
    outline-offset: 2px;
  }
  textarea { min-height: 100px; resize: vertical; }
  .chips { display: flex; flex-wrap: wrap; gap: 0.5rem; }
  .chip { position: relative; }
  .chip input { position: absolute; opacity: 0; pointer-events: none; }
  .chip span {
    display: inline-block;
    padding: 0.55rem 0.85rem;
    border: 1px solid var(--border);
    border-radius: 999px;
    font-size: 0.85rem;
    cursor: pointer;
    transition: background 0.15s, border-color 0.15s;
    user-select: none;
  }
  .chip input:focus-visible + span {
    outline: 2px solid var(--gold);
    outline-offset: 2px;
  }
  .chip input:checked + span {
    background: rgba(201, 169, 110, 0.2);
    border-color: var(--gold);
    color: var(--gold-light);
  }
  .chip input:hover + span { border-color: var(--gold-light); }
  .checks .chip span { border-radius: 8px; }
  .submit-row { margin-top: 2rem; }
  button[type="submit"] {
    width: 100%;
    padding: 1rem 1.25rem;
    border: none;
    border-radius: 6px;
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
    color: var(--black);
    font-size: 1rem;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
  }
  .note {
    font-size: 0.78rem;
    color: var(--grey-light);
    margin-top: 1rem;
    line-height: 1.45;
  }
  .success {
    display: none;
    text-align: center;
    padding: 2.5rem 1rem;
    border: 1px solid var(--border);
    border-radius: 10px;
    background: var(--surface);
  }
  .success.visible { display: block; }
  .success h2 {
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
    color: var(--gold-light);
  }
  .success p { color: var(--grey-light); font-size: 0.95rem; }
  .form-shell.hidden { display: none; }
  @media (max-width: 400px) { h1 { font-size: 1.25rem; } }
"""

def main() -> None:
    html_parts = [
        '<!DOCTYPE html>\n<html lang="ko">\n<head>\n',
        '<meta charset="UTF-8">\n',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
        '<title>',
        "\u0031\uae30 \ucc38\uac00 \uc2e0\uccad \u00b7 The AI Inner Circle",
        '</title>\n',
        '<meta name="description" content="The AI Inner Circle ',
        "\u0031\uae30 \ucc38\uac00 \uc0ac\uc804 \uc2e0\uccad\uc11c\uc785\ub2c8\ub2e4. \uc81c\ucd9c \ud6c4 \uac1c\ubcc4 \uc5f0\ub77d\uc744 \ub4dc\ub9bd\ub2c8\ub2e4.",
        '">\n',
        '<meta name="theme-color" content="#080808">\n',
        '<link rel="canonical" href="https://imhen97.github.io/ai-inner-circle/apply.html">\n',
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n',
        '<link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">\n',
        "<style>",
        CSS,
        "</style>\n</head>\n<body>\n",
        '  <div class="wrap">\n',
        '    <a class="back" href="index.html">',
        "\u2190 \ud504\ub85c\uadf8\ub7a8 \uc18c\uac1c\ub85c \ub3cc\uc544\uac00\uae30",
        '</a>\n\n',
        '    <div id="success-panel" class="success" role="status" aria-live="polite">\n',
        '      <h2>',
        "\uc2e0\uccad\uc774 \uc811\uc218\ub418\uc5c8\uc2b5\ub2c8\ub2e4",
        '</h2>\n',
        '      <p>',
        "\uc18c\uc911\ud55c \uc2dc\uac04 \ub0b4\uc5b4 \uc8fc\uc154\uc11c \uac10\uc0ac\ud569\ub2c8\ub2e4.",
        '<br>',
        "\ube60\ub974\uac8c \uac1c\ubcc4 \uc5f0\ub77d\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4.",
        '</p>\n',
        '      <hr class="sep" style="margin:1.5rem 0;">\n',
        '      <a class="back" href="index.html">',
        "\uc18c\uac1c \ud398\uc774\uc9c0\ub85c",
        '</a>\n',
        '    </div>\n\n',
        '    <div id="form-shell" class="form-shell">\n',
        '      <p class="head-badge">The AI Inner Circle</p>\n',
        '      <h1>',
        "\u0031\uae30 \ucc38\uac00 \uc0ac\uc804 \uc2e0\uccad",
        '</h1>\n',
        '      <p class="lead">',
        "\uc544\ub798 \uc591\uc2dd\uc744 \uc791\uc131\ud574 \uc8fc\uc2dc\uba74 \uc2e0\uccad \uc21c\uc73c\ub85c \uc5f0\ub77d\ub4dc\ub9bd\ub2c8\ub2e4. ",
        "\u0031\uae30\ub294 2026\ub144 5\uc6d4 4\uc77c(\uc6d4) \uc2dc\uc791 \uc608\uc815\uc774\uba70, \ud22c\uc790 \uc548\ub0b4\ub294 \uc18c\uac1c \ud398\uc774\uc9c0\uc640 \ub3d9\uc77c\ud569\ub2c8\ub2e4.",
        '</p>\n\n',
        '      <form action="https://formsubmit.co/imhen97@kakao.com" method="POST">\n',
        '        <input type="hidden" name="_subject" value="[AI Inner Circle] ',
        "\u0031\uae30 \ucc38\uac00 \uc2e0\uccad",
        '">\n',
        '        <input type="hidden" name="_template" value="table">\n',
        '        <input type="hidden" name="_next" value="https://imhen97.github.io/ai-inner-circle/apply.html?thanks=1">\n\n',
        '        <div class="block-title">',
        "\uc720\uc785 \uacbd\ub85c",
        '</div>\n',
        '        <p class="field-label">',
        "\uc5b4\ub514\uc11c \uc54c\uac8c \ub418\uc168\ub098\uc694? ",
        '<span class="req">*</span></p>\n',
        '        <div class="chips" role="radiogroup" aria-label="',
        "\uc720\uc785 \uacbd\ub85c",
        '">\n',
        '          <label class="chip"><input type="radio" name="referral" value="homepage" required><span>',
        "\ud648\ud398\uc774\uc9c0",
        '</span></label>\n',
        '          <label class="chip"><input type="radio" name="referral" value="friend"><span>',
        "\uc9c0\uc778 \uc18c\uac1c",
        '</span></label>\n',
        '          <label class="chip"><input type="radio" name="referral" value="sns"><span>SNS</span></label>\n',
        '          <label class="chip"><input type="radio" name="referral" value="search"><span>',
        "\uac80\uc0c9",
        '</span></label>\n',
        '          <label class="chip"><input type="radio" name="referral" value="other"><span>',
        "\uae30\ud0c0",
        '</span></label>\n',
        '        </div>\n',
        '        <label class="field-label" for="referral-detail" style="margin-top:1rem;">',
        "\uae30\ud0c0 \uc0c1\uc138 (\uc120\ud0dd)",
        '</label>\n',
        '        <input id="referral-detail" type="text" name="referral_detail" placeholder="',
        "\uae30\ud0c0 \uc120\ud0dd \uc2dc \uac04\ub2e8\ud788 \uc801\uc5b4 \uc8fc\uc138\uc694",
        '" autocomplete="off">\n\n',
        '        <hr class="sep">\n\n',
        '        <div class="block-title">',
        "\uae30\ubcf8 \uc815\ubcf4",
        '</div>\n',
        '        <label class="field-label" for="f-name">',
        "\uc131\ud568 ",
        '<span class="req">*</span></label>\n',
        '        <input id="f-name" type="text" name="name" required autocomplete="name" placeholder="',
        "\uc2e4\uba85",
        '">\n\n',
        '        <label class="field-label" for="f-phone" style="margin-top:1rem;">',
        "\uc5f0\ub77d\ucc98 ",
        '<span class="req">*</span></label>\n',
        '        <input id="f-phone" type="tel" name="phone" required autocomplete="tel" placeholder="010-0000-0000">\n',
        '        <p class="hint">',
        "\uc548\ub0b4\ub97c \ub4dc\ub9ac\uae30 \uc704\ud55c \uc5f0\ub77d\ucc98\uc785\ub2c8\ub2e4.",
        '</p>\n\n',
        '        <label class="field-label" for="f-email" style="margin-top:1rem;">',
        "\uc774\uba54\uc77c (\uc120\ud0dd)",
        '</label>\n',
        '        <input id="f-email" type="email" name="email" autocomplete="email" placeholder="name@example.com">\n\n',
        '        <hr class="sep">\n\n',
        '        <div class="block-title">',
        "\uc18c\uc18d \u00b7 \uc5ed\ud560",
        '</div>\n',
        '        <label class="field-label" for="f-role">',
        "\uc9c1\ud568 / \uc5ed\ud560 ",
        '<span class="req">*</span></label>\n',
        '        <input id="f-role" type="text" name="role" required placeholder="',
        "\uc608: \ub300\ud45c, \ubcc0\ud638\uc0ac, \uc6d0\uc7a5",
        '">\n\n',
        '        <label class="field-label" for="f-company" style="margin-top:1rem;">',
        "\ud68c\uc0ac\u00b7\uae30\uad00\uba85 (\uc120\ud0dd)",
        '</label>\n',
        '        <input id="f-company" type="text" name="company" placeholder="',
        "\ubc95\uc778\u00b7\uac1c\uc778 \uc0ac\uc5c5\uc790\uba85 \ub4f1",
        '">\n\n',
        '        <label class="field-label" for="f-industry" style="margin-top:1rem;">',
        "\uc5c5\uc885 / \uc8fc\uc694 \uc0ac\uc5c5 ",
        '<span class="req">*</span></label>\n',
        '        <input id="f-industry" type="text" name="industry" required placeholder="',
        "\uac04\ub2e8\ud788 \uc801\uc5b4 \uc8fc\uc138\uc694",
        '">\n\n',
        '        <hr class="sep">\n\n',
        '        <div class="block-title">',
        "\ud504\ub85c\uadf8\ub7a8 \uad00\ub828",
        '</div>\n',
        '        <p class="field-label">',
        "\ud604\uc7ac \uc5c5\ubb34\uc5d0\uc11c AI \ud65c\uc6a9 \uc815\ub3c4 ",
        '<span class="req">*</span></p>\n',
        '        <div class="chips" role="radiogroup" aria-label="AI ',
        "\ud65c\uc6a9 \uc815\ub3c4",
        '">\n',
        '          <label class="chip"><input type="radio" name="ai_level" value="none" required><span>',
        "\uac70\uc758 \uc5c6\uc74c",
        '</span></label>\n',
        '          <label class="chip"><input type="radio" name="ai_level" value="some"><span>',
        "\uc77c\ubd80 \uc0ac\uc6a9",
        '</span></label>\n',
        '          <label class="chip"><input type="radio" name="ai_level" value="active"><span>',
        "\uc801\uadf9 \ud65c\uc6a9",
        '</span></label>\n',
        '        </div>\n\n',
        '        <label class="field-label" for="f-goal" style="margin-top:1rem;">',
        "\uc774\ubc88 \u0031\uae30\uc5d0\uc11c \uac00\uc7a5 \uae30\ub300\ud558\ub294 \uac83 ",
        '<span class="req">*</span></label>\n',
        '        <textarea id="f-goal" name="goal" required placeholder="',
        "\uc608: \ubc18\ubcf5 \uc5c5\ubb34 \uc790\ub3d9\ud654, \uace0\uac1d \ub300\uc751, \ubb38\uc11c\u00b7\ub9ac\uc11c\uce58 \ub4f1",
        '"></textarea>\n\n',
        '        <p class="field-label" style="margin-top:1rem;">',
        "\uc624\ud504\ub77c\uc778 \ud074\ub798\uc2a4 \uac00\ub2a5 \uc2dc\uac04 (\ubcf5\uc218 \uc120\ud0dd)",
        '</p>\n',
        '        <div class="chips checks">\n',
        '          <label class="chip"><input type="checkbox" name="offline_pref" value="wed_1830"><span>',
        "\uc218 18:30",
        '</span></label>\n',
        '          <label class="chip"><input type="checkbox" name="offline_pref" value="sat_1400"><span>',
        "\ud1a0 14:00",
        '</span></label>\n',
        '          <label class="chip"><input type="checkbox" name="offline_pref" value="sun_1400"><span>',
        "\uc77c 14:00",
        '</span></label>\n',
        '          <label class="chip"><input type="checkbox" name="offline_pref" value="online"><span>',
        "\uc628\ub77c\uc778 \uc704\uc8fc",
        '</span></label>\n',
        '        </div>\n\n',
        '        <label class="field-label" for="f-notes" style="margin-top:1rem;">',
        "\ucd94\uac00\ub85c \uc804\ud558\uace0 \uc2f6\uc740 \ub9d0 (\uc120\ud0dd)",
        '</label>\n',
        '        <textarea id="f-notes" name="notes" placeholder="',
        "\uc77c\uc815 \uc81c\uc57d, \ubb38\uc758 \uc0ac\ud56d \ub4f1",
        '"></textarea>\n\n',
        '        <div class="submit-row">\n',
        '          <button type="submit">',
        "\uc2e0\uccad\uc11c \uc81c\ucd9c\ud558\uae30",
        '</button>\n',
        '        </div>\n',
        '        <p class="note">',
        "\uc81c\ucd9c \ub0b4\uc6a9\uc740 \ucc38\uac00 \uc0c1\ub2f4 \ubaa9\uc801\uc73c\ub85c\ub9cc \uc0ac\uc6a9\ub429\ub2c8\ub2e4. ",
        "FormSubmit\uc744 \ud1b5\ud574 \uc704 \uc218\uc2e0 \uba54\uc77c\ub85c \uc804\ub2ec\ub429\ub2c8\ub2e4. ",
        "\uccab \uc81c\ucd9c \uc804 formsubmit.co\uc5d0\uc11c \uc778\uc99d \uba54\uc77c\uc744 \ud655\uc778\ud574 \uc8fc\uc138\uc694.",
        '</p>\n',
        '      </form>\n',
        '    </div>\n',
        '  </div>\n\n',
        '  <script>\n',
        '    (function () {\n',
        '      var params = new URLSearchParams(window.location.search);\n',
        "      if (params.get('thanks') === '1') {\n",
        "        document.getElementById('success-panel').classList.add('visible');\n",
        "        document.getElementById('form-shell').classList.add('hidden');\n",
        '      }\n',
        '    })();\n',
        '  </script>\n',
        '</body>\n</html>\n',
    ]

    text = "".join(html_parts)
    OUT.write_text(text, encoding="utf-8")
    assert "\ud648\ud398\uc774\uc9c0" in text
    print("Wrote", OUT, "chars", len(text))


if __name__ == "__main__":
    main()
