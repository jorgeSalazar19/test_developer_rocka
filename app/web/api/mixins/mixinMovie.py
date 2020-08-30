
class MovieMixin(object):
    """this mixin filter queryset before retorn api
    """

    def dispatch(self, request, *args, **kwargs):
        print(self.queryset)
        return super(MovieMixin, self).dispatch(request, *args, **kwargs)
