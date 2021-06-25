from flask import jsonify


def read_sample_vioscreen_session(account_id, source_id, sample_id, **kwargs):
    with Transaction() as t:
        vio_repo = VioscreenXXX(t)
        vio_sess = VioscreenSession(t)

        vio_username = vio_repo.get_user_from_registry(account_id, source_id, sample_id)
        if vio_username is None:
            return jsonify(code=404, message="Session not found"), 404

        vio_session = vio_sess.get_session_from_username(vio_sess)
        if vio_session is None:
            # asdasdasd

        return jsonify(vio_session.to_api()), 200
