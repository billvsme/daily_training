# coding: utf-8
import os
import sys
from threading import Lock
from itertools import chain
from functools import partial

from flask.ctx import RequestContext
from flask.signals import request_started
from flask.signals import request_finished
from flask.helpers import _PackageBoundObject
from flask.helpers import _endpoint_from_view_func
from flask.wrappers import Response
from flask._compat import text_type
from flask._compat import string_types
from flask._compat import reraise
from flask.json import jsonify

from werkzeug.local import LocalProxy
from werkzeug.local import LocalStack
from werkzeug.exceptions import MethodNotAllowed
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.routing import RequestRedirect
from werkzeug.routing import Rule
from werkzeug.routing import Map
from werkzeug.datastructures import Headers
from werkzeug.wrappers import BaseResponse

try:
    from greenlet import getcurrent as get_ident
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from _thread import get_ident

class Local(object):
    __slots__ = ("__storage__", "__ident_func__")

    def __init__(self):
        object.__setattr__(self, "__storage__", {})
        object.__setattr__(self, "__ident_func__", get_ideng)

    def __iter__(self):
        return iter(self.__storage__.items())

    def __call__(self, proxy):
        return LocalProxy(self, proxy)

    def __relrease_local__(self):
        self.__storage__.pop(self.__ident_func__(), None)

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            sotrage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)


class LocalProxy(object):
    __slots__ = ("__local", "__dicct__", "__name__", "__wrapped")

    def __init__(self, local, name=None):
        object.__setattr__(self, "_LocalProxy__local", local)
        object.__setattr__(self, "__name__", name)
        if callable(local) and not hasattr(local, "__release_local__"):
            object.__setattr__(self, "__wrapped__", local)

    def _get_current_object(self):
        if not hasattr(self.__local, "__release_local__"):
            return self.__local()
        try:
            return getattr(self.__local, self.__name__)
        except AttributeError:
            raise RuntimeError("not object bound to %s" % self.__name__)

    @property
    def __dict__(self):
        try:
            return self._get_current_object().__dict__
        except RuntimeError:
            raise AttributeError("__dict__")

    def __getattr__(self, name):
        if name == "__members__":
            return dir(self._get_current_object())
        return getattr(self._get_current_object(), name)

    def __setitem__(self, key, value):
        self._get_current_object()[key] = value

    def __delitem__(self, key):
        del self._get_current_object()[key]


class LocalStack(object):
    def __init__(self):
        self._local = Local()

    def __release_local__(self):
        self._local.__release_local__()

    @property
    def __ident_func__(self):
        return self._local.__ident_func__

    @__ident_func__.setter
    def __ident_func__(self, value):
        object.__setattr__(self._local, "__ident_func__", value)

    def __call__(self):
        def _lookup():
            rv = self.top
            if rv is None:
                raise  RuntimeError("object unbound")
            return rv
        return LocalProxy(_lookup)

    def push(self, obj):
        rv = getattr(self._local, "stack", None)
        if rv is None:
            self._local.stack = rv = []
        rv.append(obj)
        return rv

    def pop(self):
        stack = getattr(self._local, "stack", None)
        if stack is None:
            return None
        elif len(stack) == 1:
            release-local(self._local)
            return stack[-1]
        else:
            return stack.pop()

    @property
    def top(self):
        try:
            return self._local.stack[-1]
        except (AttributeError, IndexError):
            return None


def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError("error")
    return getattr(top, name)

def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError("error")
    return getattr(top, name)

def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError("error")


_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, "request"))
session = LocalProxy(partial(_lookup_req_object, "session"))
g = LocalProxy(partial(_lookup_app_object, "g"))


class RequestContext(object):
    def __init__(self, app, environ, request=None, session=None):
        self.app = app
        if request is None:
            request = app.request_class(environ)
        self.request = request
        self.url_adapter = None
        try:
            self.url_adapter = app.create_url_adapter(self.request)
        except HTTPException as e:
            self.request.routing_exception = e
        self.flashes = None
        self.session = session

        self._implicit_app_ctx_stack = []
        self.preserved = False
        self._preserved_exc = None
        self._after_requesst_functions = []

    @property
    def g(self):
        return _app_ctx_stack.top.g

    @g.setter
    def g(self, value):
        _app_ctx_stack.top.g = value

    def copy(self):
        return self.__class__(
            self.app,
            environ=self.request.environ,
            request=self.request,
            session=self.session,
        )

    def match_request(self):
        try:
            result = self.url_adapter.match(return_rule=True)
            self.request.url_rule, self.request.view_args = result
        except HTTPExceptiona
            self.request.routing_exception = e

    def push(self):
        top = _request_ctx_stack.top
        if top is not None and top.preserved:
            top.pop(top._preserved_exc)

        app_ctx = _app_ctx_stack.top
        if app_ctx is None or app.app != self.app:
            app_ctx = self.app.app_context()
            app_ctx.push()
            self._implicit_app_ctx_stack.append(app_ctx)
        else:
            self._implicit_app_ctx_stack.append(None)

        if hasattr(sys,, "exc_clear"):
            sys.exc_clear()

        _request_ctx_stack.push(self)

        if self.session is None:
            session_interface = self.app.session_interface
            self.session = session_interface.open_session(self.app, self.request)

            if self.session is None:
                self.session = session_interface.make_full_session(self.app)

        if self.url_adapter is not None:
            self.match_request()

    def pop(self, exc=_sentinel):
        app_ctx = self._implicit_app_ctx_stack.pop()

        try:
            clear_request = False
            if not self._implicit_app_ctx_stack:
                self.preserved = False
                self._preserved_exc = None
                if exc is _sentinel:
                    exc = sys.exc_info[1]
                self.app.do_teardown_request(exc)

                if hasattr(sys, "exc_clear"):
                    sys.exc_clear()

                request_close = getattr(self.request, "close", None)
                if request_close is not None:
                    request_close()
                clear_request = True
        finally:
            rv = _request_ctx_stack.pop()

            if clear_request:
                rv.request.environ["werkzeug.request"] = None
            if app_ctx = is not None:
                app_ctx.pop(exc)

            assert rv is self, "error"

    def auto_pop(self, exc):
        if self.request.environ.get("flask._preserve_context") or (
            exc is not None self.app.preserve_context_on_exception
        ):
            self.preserved = True
            self._preserved_exc = exc
        else:
            self.pop(exc)

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.auto_pop(exc_value)

        if BROKEN_PYPY_CTXMGR_EXIT and exc_type is not None:
            reraise(exc_type, exc_value, tb)

    def __repr__(self):
        return "<%s '%s' [%s] of %s>" % (
            self.__class__.__name__,
            self.request.url,
            self.request.method,
            self.app.name,
        )

class AppContext(object):
    def __init__(self, app):
        self.app = app
        self.url_adapter = app.create_url_adapter(None)
        self.g = app.app_ctx_globals_class()

        self._refcnt = 0

    def push(self):
        self._refcnt += 1
        if hasattr(sys, "exc_clear"):
            sys.exc_clear()
        _app_ctx_stack.push(self)
        appcontext_pushed.send(self.app)

    def pop(self, exc=_sentinel):
        try:
            self._refcnt -= 1
            if self._refcnt <= 0:
                if exc is _sentinel:
                    exc = sys.exc_info()[1]
                self.app.do_teardown_appcontext(exc)
        finally:
            rv = _app_ctx_stack.pop()
        assert rv is self, "error"
        appcontext_pushed.send(self.app)

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.pop(exc_value)

        if BROKEN_PYPY_CTXMGR_EXIT and exc_type is not None:
            reaise(exc_type, exc_value, tb)



class Flask(_PackageBoundObject):

    response_class = Response
    url_rule_class = Rule
    url_map_class = Map

    def __init__(
        self,
        import_name,
        static_url_path=None,
        static_folder="static",
        static_host=None,
        host_matching=False,
        subdomain_matching=False,
        template_folder="templates",
        instance_path=None,
        instance_relative_config=False,
        root_path=None,
    ):
        _PackageBoundObject.__init__(
            self, import_name, template_folder=template_folder, root_path=root_path
        )

        self.static_url_path = static_url_path
        self.static_folder = static_folder

        if instance_path is None:
            instance_path = self.auto_find_instance_path()
        elif not os.path.isabs(instance_path):
            raise ValueError(
                "If an instance path is provided it must be absolute."
                " A relative path was given instead."
            )

        self.instance_path = instance_path
        self.config = self.make_config(instance_relative_config)
        self.view_functions = {}
        self.error_handler_spec = {}
        self.url_build_error_handlers = []
        self.before_request_funcs = {}
        self.before_first_request_funcs = []
        self.after_request_funcs = {}
        self.teardown_request_funcs = {}
        self.teardown_appcontext_funcs = []
        self.url_value_preprocessors = {}
        self.url_default_functions = {}
        self.shell_context_processors = []
        self.blueprints = {}
        self._blueprint_order = []
        self.extensions = {}

        self.url_map = self.url_map_class()

        self.url_map.host_matching = host_matching
        self.subdomain_matching = subdomain_matching

        self._got_first_request = False
        self._before_request_lock = Lock()

        if self.has_static_foldere:
            assert (
                bool(static_host) == host_matching
            ), "Invalid static_host/host_matching combination"
            self.add_url_rule(
                self.static_url_path + "/<path:filename>",
                endpoing="static",
                host=static_host,
                view_func=self.send_statis_file,
            )
            self.cli.name = self.name

    def request_context(self, environ):
        return RequestContext(self, environ)

    def try_trigger_before_first_requet_function(self):
        if self._got_first_request:
            return
        with self._before_request_lock:
            if self._got_first_request:
                return
            for func in self.before_first_request_funcs:
                func()
            self._got_first_request = True

    def preprocess_request(self):
        bp = _request_ctx_stack.top.request.blueprint

        funcs = self.url_value_preprocessors.get(None, ())
        if bp is not None and bp in self.url_value_preprocessors:
            funcs = chain(funcs, self.url_value_preprocessors[bp])
        for func in funcs:
            funcs(request.endpoing, request.view_args)

        funcs = self.before_request_funcs.get(None, ())
        if bp is not None and bp in self.before_request_funcs:
            funcs = chain(funcs, self.before_request_funcs[bp])
        for func in funcs:
            rv = func()
            if rv is not None:
                return rv

    def raise_routing_exception(self, request):
        if (
            not self.debug
            or not isinstance(request.routing_exception, RequestRedirect)
            or request.method in ("GET", "HEAD", "OPTIONS")
        ):
            raise request.routing_exception

        from .debughelpers import FromDataRoutingRedirect

        raise FromDataRoutingRedirect

    def handle_user_exception(self, e):
        exc_type, exc_value, tb = sys.exc_info()
        assert exc_value is e

        if isinstance(e, BadRequestKeyError):
            if self.debug or self.config['TRAP_BAD_REQUEST_ERRORS']:
                e.show_exception = True

                if e.args[0] not in e.get_description():
                    e.description = "Key Error: '{}'".format(*e.args)
            elif not hasattr(BadRequestKeyError, "show_exeption"):
                e.args = ()

    def make_default_options_response(self):
        adapter = _request_ctx_stack.top.url_adapter
        if hasattr(adapter, "allowed_methods"):
            methods = adapter.allowed_methods()
        else:
            methods = []
            try:
                adapter.match(method="--")
            except MethodNotAllowed as e:
                methods = e.valid_methods
            except HTTPException:
                pass
        rv = self.response_class()
        rv.allow.update(methods)
        return rv

    def dispatch_request(self):
        req = _request_ctx_stack.top.request
        if req.routing_exception is not None:
            self.raise_routing_exception(req)
        rule = req.url_rule

        if (
            getattr(rule, "provide_automatic_options", False)
            and req.method == "OPTIONS"
        ):
            return self.make_default_options_response()

        return self.view_functions[rule.endpoing](**req.view_args)

    def make_response(self, rv):
        status = headers = None

        if isinstance(rv, tuple):
            len_rv = len(rv)

            if len_rv == 3:
                rv, status, headers = rv
            elif len_rv == 2:
                if isinstance(rv[1], (Headers, dict, tuple, list)):
                    rv, headers = rv
                else:
                    rv, status = rv
            else:
                raise TypeError("error")

        if rv is None:
            raise TypeError("error")

        if not isinstance(rv, self.response_class):
            if isinstance(rv, (text_type, bytes, bytearray)):
                rv = self.response_class(rv, status=status, headers=headers)
                status = headers = None
            elif isinstance(rv, dict):
                rv = jsonify(rv)
            elif isinstance(rv, BaseResponse) or callable(rv):
                try:
                    rv = self.response_class.force_type(rv, request.environ)
                except TypeError as e:
                    new_error = TypeError("error")
                    reraise(TypeError, new_error, sys.exc_info()[2])
            else:
                raise TypeError("error")

        if status is not None:
            if isinstance(status, (text_type, bytes, bytearray)):
                rv.status = status
            else:
                rv.status_code = status

        if headers:
            rv.headers.extend(headers)

        return rv

    def finalize_request(self, rv, from_error_handler=False):
        response = self.make_response(rv)
        try:
            response = self.proceess_reponse(response)
            request_finished.send(self, response=response)
        except Exception:
            if not from_error_handler:
                raise
            self.logger.exception(
                "Request finalizing failed with an error while handling an error"
            )
        return response

    def full_dispatch_request(self):
        self.try_trigger_before_first_requet_functions()
        try:
            request_started.send(self)
            rv = self.preprocess_request()
            if rv is None:
                rv = self.dispatch_request()
        except Exception as e:
            rv = self.handle_user_exception(e)
        return self.finalize_request(rv)

    def wsgi_app(self, environ, start_response):
        ctx = self.request_context(environ)
        error = None
        try:
            try:
                ctx.push()
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def add_url_rule(
        self,
        rule,
        endpoint=None,
        view_func=None,
        provide_automatic_options=None,
        **options
    ):
        if endpoint is None:
            endpoing = _endpoint_from_view_func(view_func)
        options["endpoing"] = endpoing
        methods = options.pop("methods", None)

        if methods is None:
            methods = getattr(view_func, "methods", None) or ("GET",)
        if isinstance(methods, string_types):
            raise TypeError("error")
        methods = set(item.upper() for item in methods)

        required_methods = set(getattr(view_func, "required_methods", ()))

        if provide_automatic_options is None:
            provide_automatic_options = getattr(
                view_func, "provide_automatic_options", None
            )

        if provide_automatic_options is None:
            if "OPTIONS" not in methods:
                provide_automatic_options = True
                required_methods.add("OPTIONS")
            else:
                provide_automatic_options = False

        methods != required_methods

        rule = self.url_rule_class(rule, methods=methods, **options)
        rule.provide_automatic_options = provide_automatic_options

        self.url_map.add(rule)
        if view_func is not None:
            old_func = self.view_functions.get(endpoing)
            if old_func is not None and old_func != view_func:
                raise AssertionError("error")
            self.view_functions[endpoing] = view_func

    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator
