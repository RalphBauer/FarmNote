import Cookies from 'js-cookie';
import {NotesApi} from "http-client";

class NoteService {
    notesApi = new NotesApi();

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
        try {
            const token = Cookies.get("session_token");
            let notes = await this.notesApi.readNotes({
                token: token
            });
            return notes;
        } catch (error) {
            throw new Error('NoteService: Failed to fetch notes: ' + error.message);
        }
    }

    // Methode zum Aktualisieren einer Notiz
    async updateNote(noteId, noteData, token) {
        try {
            console.log("NoteService:", noteId);

            // Überprüfen, ob noteData ein gültiges Objekt ist
            if (!noteData || typeof noteData !== 'object') {
                throw new Error('Invalid noteData provided');
            }
            console.log(noteData)

            // API-Aufruf zur Aktualisierung der Notiz
            const updatedNote = await this.notesApi.updateNote({
                noteId: noteId,
                token: token,
                noteUpdate: {
                    id: noteId,
                    ...noteData,
                }
            });

            return updatedNote; // Rückgabe der aktualisierten Notiz
        } catch (error) {
            console.error('Error details:', error); // Detaillierte Fehlermeldung
            throw new Error('NoteService: Failed to update note: ' + error.message);
        }
    }

    async deleteNote(noteId, token) {
        try {
            console.log("NoteService: Deleting note with ID:", noteId);

            // API-Aufruf zum Löschen der Notiz
            await this.notesApi.deleteNote({
                noteId: noteId,
                token: token
            });

            return {message: 'Note deleted successfully'}; // Erfolgsnachricht zurückgeben
        } catch (error) {
            console.error('Error details:', error); // Detaillierte Fehlermeldung
            throw new Error('NoteService: Failed to delete note: ' + error.message);
        }
    }

}

export default new NoteService();
