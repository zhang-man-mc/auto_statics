
class ColumnDelete:
    authentication_delete_max_col = 13
    commitment_delete_max_col = 12
    ledger_delete_max_col = 12
    score_delete_max_col = 9
    user_login_delete_max_col = 8

    def get_sheets_delete_cols():
        return [ColumnDelete.user_login_delete_max_col,ColumnDelete.score_delete_max_col,ColumnDelete.ledger_delete_max_col,ColumnDelete.commitment_delete_max_col,ColumnDelete.authentication_delete_max_col]