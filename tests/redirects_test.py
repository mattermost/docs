"""
Redirect tests
"""
import pytest
from extensions.reredirects import (
    setup as ext_setup,
    builder_inited as ext_builder_inited,
    CONFIG_OPTION_REDIRECTS,
    CONFIG_OPTION_TEMPLATE_FILE,
    CONFIG_MM_URL_PATH_PREFIX,
    CONFIG_WRITE_EXTENSIONLESS_PAGES,
    ENV_COMPUTED_REDIRECTS,
    ENV_REDIRECTS_ENABLED
)
from typing import Dict


def test_setup(app):
    result = ext_setup(app)
    assert "parallel_read_safe" in result
    assert result["parallel_read_safe"]
    assert "parallel_write_safe" in result
    assert result["parallel_write_safe"]
    assert hasattr(app.config, CONFIG_OPTION_REDIRECTS)
    assert hasattr(app.config, CONFIG_OPTION_TEMPLATE_FILE)
    assert hasattr(app.config, CONFIG_MM_URL_PATH_PREFIX)
    assert hasattr(app.config, CONFIG_WRITE_EXTENSIONLESS_PAGES)


class TestBuilderInited:
    def test_nominal(self, app):
        ext_setup(app)
        app.config[CONFIG_OPTION_REDIRECTS] = dict({"foo": "bar"})
        ext_builder_inited(app)
        assert(hasattr(app.env, ENV_COMPUTED_REDIRECTS))
        computed_redirects: Dict[str, str] = getattr(app.env, ENV_COMPUTED_REDIRECTS)
        assert(len(computed_redirects) == 1)

    def test_no_config_value(self, app):
        ext_setup(app)
        app.config[CONFIG_OPTION_REDIRECTS] = None
        ext_builder_inited(app)
        assert(not getattr(app.env, ENV_REDIRECTS_ENABLED))
        assert(not hasattr(app.env, ENV_COMPUTED_REDIRECTS))

    def test_empty_config_value(self, app):
        ext_setup(app)
        app.config[CONFIG_OPTION_REDIRECTS] = dict()
        ext_builder_inited(app)
        assert(not getattr(app.env, ENV_REDIRECTS_ENABLED))
        assert(not hasattr(app.env, ENV_COMPUTED_REDIRECTS))


class TestEnvUpdated:
    def test_nominal(self, app):
        ext_setup(app)
        app.env.all_docs["foo"] = 0
        app.config[CONFIG_OPTION_REDIRECTS] = dict({"foo": "bar"})
        ext_builder_inited(app)
