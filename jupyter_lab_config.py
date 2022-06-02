# Configuration file for lab.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------

## Base class for Jupyter applications

## Answer yes to any prompts.
#c.JupyterApp.answer_yes = False

## Full path of a config file.
#c.JupyterApp.config_file = ''

## Specify a config file to load.
#c.JupyterApp.config_file_name = ''

## Generate default config file.
#c.JupyterApp.generate_config = False

#------------------------------------------------------------------------------
# ExtensionApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## Base class for configurable Jupyter Server Extension Applications.
#  
#  ExtensionApp subclasses can be initialized two ways:
#  1. Extension is listed as a jpserver_extension, and ServerApp calls
#      its load_jupyter_server_extension classmethod. This is the
#      classic way of loading a server extension.
#  2. Extension is launched directly by calling its `launch_instance`
#      class method. This method can be set as a entry_point in
#      the extensions setup.py

## 
#c.ExtensionApp.default_url = ''

## Handlers appended to the server.
#c.ExtensionApp.handlers = []

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (ServerApp.browser)
#  configuration option.
#c.ExtensionApp.open_browser = False

## Settings that will passed to the server.
#c.ExtensionApp.settings = {}

## paths to search for serving static files.
#  
#  This allows adding javascript/css to be available from the notebook server
#  machine, or overriding individual files in the IPython
#c.ExtensionApp.static_paths = []

## Url where the static assets for the extension are served.
#c.ExtensionApp.static_url_prefix = ''

## Paths to search for serving jinja templates.
#  
#  Can be used to override templates from notebook.templates.
#c.ExtensionApp.template_paths = []

#------------------------------------------------------------------------------
# LabServerApp(ExtensionAppJinjaMixin,LabConfig,ExtensionApp) configuration
#------------------------------------------------------------------------------

## A Lab Server Application that runs out-of-the-box

## "A list of comma-separated URIs to get the allowed extensions list
#  
#  .. versionchanged:: 2.0.0
#      `LabServerApp.whitetlist_uris` renamed to `allowed_extensions_uris`
#c.LabServerApp.allowed_extensions_uris = ''

## Deprecated, use `LabServerApp.blocked_extensions_uris`
#c.LabServerApp.blacklist_uris = ''

## A list of comma-separated URIs to get the blocked extensions list
#  
#  .. versionchanged:: 2.0.0
#      `LabServerApp.blacklist_uris` renamed to `blocked_extensions_uris`
#c.LabServerApp.blocked_extensions_uris = ''

## The interval delay in seconds to refresh the lists
#c.LabServerApp.listings_refresh_seconds = 3600

## The optional kwargs to use for the listings HTTP requests             as
#  described on https://2.python-requests.org/en/v2.7.0/api/#requests.request
#c.LabServerApp.listings_request_options = {}

## Deprecated, use `LabServerApp.allowed_extensions_uris`
#c.LabServerApp.whitelist_uris = ''

#------------------------------------------------------------------------------
# LabApp(NBClassicConfigShimMixin,LabServerApp) configuration
#------------------------------------------------------------------------------

## The app directory to launch JupyterLab from.
#c.LabApp.app_dir = None

## Whether to enable collaborative mode.
#c.LabApp.collaborative = False

## Whether to start the app in core mode. In this mode, JupyterLab will run using
#  the JavaScript assets that are within the installed JupyterLab Python package.
#  In core mode, third party extensions are disabled. The `--dev-mode` flag is an
#  alias to this to be used when the Python package itself is installed in
#  development mode (`pip install -e .`).
#c.LabApp.core_mode = False

## The default URL to redirect to from `/`
#c.LabApp.default_url = '/lab'

## Whether to start the app in dev mode. Uses the unpublished local JavaScript
#  packages in the `dev_mode` folder.  In this case JupyterLab will show a red
#  stripe at the top of the page.  It can only be used if JupyterLab is installed
#  as `pip install -e .`.
#c.LabApp.dev_mode = False

## Whether to expose the global app instance to browser via window.jupyterlab
#c.LabApp.expose_app_in_browser = False

## Whether to load prebuilt extensions in dev mode. This may be useful to run and
#  test prebuilt extensions in development installs of JupyterLab. APIs in a
#  JupyterLab development install may be incompatible with published packages, so
#  prebuilt extensions compiled against published packages may not work
#  correctly.
#c.LabApp.extensions_in_dev_mode = False

## The override url for static lab assets, typically a CDN.
#c.LabApp.override_static_url = ''

## The override url for static lab theme assets, typically a CDN.
#c.LabApp.override_theme_url = ''

## Splice source packages into app directory.
#c.LabApp.splice_source = False

## The directory for user settings.
#c.LabApp.user_settings_dir = '/root/.jupyter/lab/user-settings'

## Whether to serve the app in watch mode
#c.LabApp.watch = False

## The directory for workspaces
#c.LabApp.workspaces_dir = '/root/.jupyter/lab/workspaces'

#------------------------------------------------------------------------------
# ServerApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## Set the Access-Control-Allow-Credentials: true header
#c.ServerApp.allow_credentials = False

## Set the Access-Control-Allow-Origin header
#  
#  Use '*' to allow any origin to access your server.
#  
#  Takes precedence over allow_origin_pat.
#c.ServerApp.allow_origin = ''

## Use a regular expression for the Access-Control-Allow-Origin header
#  
#  Requests from an origin matching the expression will get replies with:
#  
#      Access-Control-Allow-Origin: origin
#  
#  where `origin` is the origin of the request.
#  
#  Ignored if allow_origin is set.
#c.ServerApp.allow_origin_pat = ''

## Allow password to be changed at login for the Jupyter server.
#  
#  While logging in with a token, the Jupyter server UI will give the opportunity
#  to the user to enter a new password at the same time that will replace the
#  token login mechanism.
#  
#  This can be set to false to prevent changing password from the UI/API.
#c.ServerApp.allow_password_change = True

## Allow requests where the Host header doesn't point to a local server
#  
#  By default, requests get a 403 forbidden response if the 'Host' header shows
#  that the browser thinks it's on a non-local domain. Setting this option to
#  True disables this check.
#  
#  This protects against 'DNS rebinding' attacks, where a remote web server
#  serves you a page and then changes its DNS to send later requests to a local
#  IP, bypassing same-origin checks.
#  
#  Local IP addresses (such as 127.0.0.1 and ::1) are allowed as local, along
#  with hostnames configured in local_hostnames.
c.ServerApp.allow_remote_access = True

## Whether to allow the user to run the server as root.
#c.ServerApp.allow_root = False

## " Require authentication to access prometheus metrics.
#c.ServerApp.authenticate_prometheus = True

## Reload the webapp when changes are made to any Python src files.
#c.ServerApp.autoreload = False

## The base URL for the Jupyter server.
#  
#  Leading and trailing slashes can be omitted, and will automatically be added.
#c.ServerApp.base_url = '/'

## Specify what command to use to invoke a web browser when starting the server.
#  If not specified, the default browser will be determined by the `webbrowser`
#  standard library module, which allows setting of the BROWSER environment
#  variable to override it.
#c.ServerApp.browser = ''

## The full path to an SSL/TLS certificate file.
#c.ServerApp.certfile = ''

## The full path to a certificate authority certificate for SSL/TLS client
#  authentication.
#c.ServerApp.client_ca = ''

## The config manager class to use
#c.ServerApp.config_manager_class = 'jupyter_server.services.config.manager.ConfigManager'

## The content manager class to use.
#c.ServerApp.contents_manager_class = 'jupyter_server.services.contents.largefilemanager.LargeFileManager'

## Extra keyword arguments to pass to `set_secure_cookie`. See tornado's
#  set_secure_cookie docs for details.
#c.ServerApp.cookie_options = {}

## The random bytes used to secure cookies. By default this is a new random
#  number every time you start the server. Set it to a value in a config file to
#  enable logins to persist across server sessions.
#  
#  Note: Cookie secrets should be kept private, do not share config files with
#  cookie_secret stored in plaintext (you can read the value from a file).
#c.ServerApp.cookie_secret = b''

## The file where the cookie secret is stored.
#c.ServerApp.cookie_secret_file = ''

## Override URL shown to users.
#  
#  Replace actual URL, including protocol, address, port and base URL, with the
#  given value when displaying URL to the users. Do not change the actual
#  connection URL. If authentication token is enabled, the token is added…
