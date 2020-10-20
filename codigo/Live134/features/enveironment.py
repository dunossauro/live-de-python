def before_all(context):
    context.base_url = context.config.userdata.get('url_base')