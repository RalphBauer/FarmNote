import {NotesApi} from "http-client";


class NoteService {
    notesApi = new NotesApi();

    async getAllNotes(token) {
        return this.notesApi.readNotes({
            token: token
        }).then(notes => {
            return notes;
        });
    }
}

export default new NoteService();