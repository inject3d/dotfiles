# Load settings configured via autoconfig.yml
config.load_autoconfig()

# Enable JavaScript for local files
config.set('content.javascript.enabled', True, 'file://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

## MPV (https://mpv.io)
config.bind('<z><m>', 'spawn --userscript view_in_mpv')

## Pass password manager (https://www.passwordstore.org)
config.bind('<z><l><l>', 'spawn --userscript qute-pass')
config.bind('<z><l><u>', 'spawn --userscript qute-pass --username-only')
config.bind('<z><l><p>', 'spawn --userscript qute-pass --password-only')
config.bind('<z><l><o>', 'spawn --userscript qute-pass --otp-only')

## Pocket (https://getpocket.com)
config.bind('<z><p>',
            'spawn --userscript ~/.config/qutebrowser/userscripts/qutepocket')

## Reading view (https://github.com/buriy/python-readability)
config.bind('<z><r>', 'spawn --userscript readability')
