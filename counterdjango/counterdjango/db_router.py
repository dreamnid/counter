from builtins import object

class DbRouter(object):
    def db_for_read(self, model, **hints):
        if model is not None and model._meta.app_label == 'counterapp' and model._meta.model_name == 'mysqlcounter':
            return 'mysql'

        return 'default'

    def db_for_write(self, model, **hints):
        if model is not None and model._meta.app_label == 'counterapp' and model._meta.model_name == 'mysqlcounter':
            return 'mysql'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True