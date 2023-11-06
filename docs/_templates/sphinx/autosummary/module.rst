.. modified from ``sphinx/ext/autosummary/templates/autosummary/module.rst

:generated:


{{ fullname | escape | underline}}

{% block modules %}
{% if modules %}
.. Modules
.. --------

.. autosummary::
   :toctree:
   :recursive:
{% for item in modules %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

.. automodule:: {{ fullname }}

   {% block overview %}
   {% if (attributes or functions or classes or exceptions) %}
   Overview
   --------
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: {{ _('Module Attributes') }}

   .. autosummary::
   {% for item in attributes %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block functions %}
   {% if functions %}
   .. rubric:: {{ _('Functions') }}

   .. autosummary::
   {% for item in functions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block classes %}
   {% if classes %}
   .. rubric:: {{ _('Classes') }}

   .. autosummary::
   {% for item in classes %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block exceptions %}
   {% if exceptions %}
   .. rubric:: {{ _('Exceptions') }}

   .. autosummary::
   {% for item in exceptions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

{% block api %}
{% if (attributes or functions or classes or exceptions) %}
API documentation
-----------------
{% endif %}
{% endblock %}

{% block attributes_api %}
{% if attributes %}
{% for item in attributes %}
.. autodata:: {{ item }}
    :annotation:
{%- endfor %}
{% endif %}
{% endblock %}

{% block function_api %}
{% if functions %}
{% for item in functions %}
.. autofunction:: {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block class_api %}
{% if classes %}
{% for item in classes %}
.. autoclass:: {{ item }}
    :show-inheritance:
    :members:
    :undoc-members:

    .. dropdown:: Class Overview
       :open:

       .. autoclasstoc::


{% endfor %}
{% endif %}
{% endblock %}

{% block exceptions_api %}
{% if exceptions %}
{% for item in exceptions %}
.. autoexception:: {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}
