from capturemock import capturemock, RECORD, REPLAY


@capturemock('sqlalchemy', mode=REPLAY)
def test_sqlalchemy():
    import sqlalchemy

    db_uri = 'mssql+pymssql://user:password@localhost/database'
    engine = sqlalchemy.create_engine(db_uri)
    conn = engine.connect()
    result = conn.execute('SELECT @@VERSION').scalar()
    expected_output = \
        'Microsoft SQL Server 2012 - 11.0.2100.60 (X64) \n' \
        + '\tFeb 10 2012 19:39:15 \n' \
        + '\tCopyright (c) Microsoft Corporation\n' \
        + '\tDeveloper Edition (64-bit) on Windows NT 6.1 <X64> ' \
        + '(Build 7601: Service Pack 1)\n'
    assert result == expected_output
