# Script main
from cat.mad_hatter.decorator import hook

#TEST

#caricare
@hook(priority = 10)
def agent_prompt_prefix(prefix, cat):
    
    settings = cat.mad_hatter.get_plugin().load_settings()
    prefix = settings["prefix"]
    return prefix