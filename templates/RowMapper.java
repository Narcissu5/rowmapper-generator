package {{ package }};

import {{ package }}.{{ name }};
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Component;

import java.sql.ResultSet;
import java.sql.SQLException;

@Component
public class {{ name }}RowMapper implements RowMapper<{{ name }}> {
    @Override
    public {{ name }} mapRow(ResultSet rs, int rowNum) throws SQLException {
        {{ name }} ret = new {{ name }}();
        {% for row in rows %}
        ret.set{{ row.first_uppercase }}(rs.get{{row.rs_type}}("{{ row.field }}")); 
        {% if row.nullable is equalto 'YES' %}
        if(rs.wasNull()) {
            ret.set{{ row.first_uppercase }}(null); 
        }
        {% endif %}
        {% endfor %}
        return ret;
    }
}

