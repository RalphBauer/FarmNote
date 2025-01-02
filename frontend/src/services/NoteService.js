import Cookies from 'js-cookie';
import {NotesApi, SessionApi} from "http-client";

class NoteService {
    notesApi = new NotesApi();
    sessionApi = new SessionApi();

    // Methode zum Erstellen einer Session
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



    // Methode zum Erstellen einer Notiz
    async createNote(noteData, token) {
        try {
            return await this.notesApi.createNote({
                token: token,
                noteCreate: noteData
            }, request => {
                return {
                    ...request.init,
                    body: {
                        ...request.init.body,
                        field_id: noteData.field_id
                    }
                };
            });
        } catch (error) {
            throw new Error('NoteService: Failed to create note: ' + error.message);
        }
    }

    // Methode zum Abrufen aller Notizen
    async getAllNotes() {
    const token = Cookies.get("session_token");
    try {
        let notes = await this.notesApi.readNotes({
            token: token
        });
        return notes;
    } catch (error) {
        throw new Error('NoteService: Failed to fetch notes: ' + error.message);
    }
}
}

export default new NoteService();
