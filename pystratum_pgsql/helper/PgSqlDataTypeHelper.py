from typing import Any, Dict

from pystratum_common.helper.DataTypeHelper import DataTypeHelper


class PgSqlDataTypeHelper(DataTypeHelper):
    """
    Utility class for deriving information based on a PostgreSQL data type.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def column_type_to_python_type(self, data_type_info: Dict[str, Any]) -> str:
        """
        Returns the corresponding Python data type of a PostgreSQL data type.

        :param dict data_type_info: The PostgreSQL data type metadata.

        :rtype: str
        """
        if data_type_info['data_type'] in ['bit',
                                           'bigint',
                                           'smallint',
                                           'integer']:
            return 'int'

        if data_type_info['data_type'] in ['boolean']:
            return 'bool'

        if data_type_info['data_type'] in ['date',
                                           'time without time zone',
                                           'timestamp without time zone']:
            return 'str'

        if data_type_info['data_type'] == 'numeric':
            return 'float|int'

        if data_type_info['data_type'] in ['real',
                                           'double',
                                           'money']:
            return 'float'

        if data_type_info['data_type'] in ['character',
                                           'character varying',
                                           'text']:
            return 'str'

        if data_type_info['data_type'] in ['bytea',
                                           'binary']:
            return 'bytes'

        raise RuntimeError('Unknown data type {0}'.format(data_type_info['data_type']))

    # ------------------------------------------------------------------------------------------------------------------
    def column_type_to_python_type_hint(self, data_type_info: Dict[str, Any]) -> str:
        """
        Returns the corresponding Python data type hinting of a PostgreSQL data type.

        :param dict data_type_info: The PostgreSQL data type metadata.

        :rtype: str
        """
        if data_type_info['data_type'] in ['bit',
                                           'bigint',
                                           'smallint',
                                           'integer']:
            return 'Optional[int]'

        if data_type_info['data_type'] in ['boolean']:
            return 'Optional[bool]'

        if data_type_info['data_type'] in ['date',
                                           'time without time zone',
                                           'timestamp without time zone']:
            return 'Optional[str]'

        if data_type_info['data_type'] == 'numeric':
            return 'Union[float, int, None]'

        if data_type_info['data_type'] in ['real',
                                           'double',
                                           'money']:
            return 'Optional[float]'

        if data_type_info['data_type'] in ['character',
                                           'character varying',
                                           'text']:
            return 'Optional[str]'

        if data_type_info['data_type'] in ['bytea',
                                           'binary']:
            return 'Optional[bytes]'

        raise RuntimeError('Unknown data type {0}'.format(data_type_info['data_type']))

# ----------------------------------------------------------------------------------------------------------------------
