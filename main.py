from pathlib import Path
import warnings
from enhanced_logger import EnhancedLogger
import logging

import flet_easy as fs
from core.config import ConfigApp

# We ignore deprecation warnings from Flet.  These are due to Flet-Easy using some deprecated Flet features
# that have not yet been updated in Flet-Easy.  These warnings will be removed in future releases of Flet-Easy.
warnings.filterwarnings("ignore", category=DeprecationWarning)

# We create the Flet-Easy application instance
app = fs.FletEasy(
    route_init="/home",
    path_views=Path(__file__).parent / "views"
    )

# We load the application configuration.
ConfigApp(app)

# We run the application
app.run( )
