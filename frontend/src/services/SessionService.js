import Cookies from 'js-cookie';
import {SessionApi} from "http-client";

class SessionService {
    sessionApi = new SessionApi();

    async createSession() {
        try {
            let response = await this.sessionApi.createSession({})
            const token_new = response.token;
            Cookies.set("session_token", token_new, {expires: 7});
            return token_new;
        } catch (error) {
            throw new Error('Error at SessionService createSession' + error);
        }
    }
}
export default new SessionService();