package {{ package }};

public class {{ name }} {
    {% for row in rows %}
    private {{row.type}} {{ row.camel }};
    {% endfor %}

    {% for row in rows %}
    public {{ row.type }} get{{ row.first_uppercase }}() {
        return this.{{ row.camel }};
    }

    public void set{{ row.first_uppercase }}({{ row.type }} {{ row.camel }}) {
        this.{{ row.camel }} = {{ row.camel }};
    }
    {% endfor %}
}