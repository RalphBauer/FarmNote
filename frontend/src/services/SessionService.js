import Cookies from 'js-cookie';
import {SessionApi} from "http-client";

class SessionService {
    sessionApi = new SessionApi();

    async createSession() {
        try {
            const response = await fetch(`${import.meta.env.VITE_API_URL}/sessions/create-session/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ length: 6 })
            });

            const data = await response.json();
            Cookies.set("session_token", data.token);
            return data;  // Wir geben die Antwort zurück, die das Token enthält
        } catch (error) {
            console.error("Fehler bei der Session-Erstellung:", error);
            throw error;
        }
    }

    // Methode zum Laden einer Session
    async loadSession(sessionId) {
        try {
            const response = await fetch(`${import.meta.env.VITE_API_URL}/sessions/load-session/?token=${sessionId}`, {
                method: 'GET', // Use GET if you're loading a session
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            // Check if the response is ok (status in the range 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Set the session token in cookies if needed
            if (data.token) {
                Cookies.set("session_token", data.token);
            }

            return data; // Return the session data
        } catch (error) {
            console.error("Error during fetch request:", error);
            throw error; // Rethrow the error for further handling
        }
    }
}
export default new SessionService();