/* tslint:disable */
/* eslint-disable */
/**
 * FarmNote
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: r206067@fhwn.ac.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
/**
 * Schema for updating an existing note
 * @export
 * @interface NoteUpdate
 */
export interface NoteUpdate {
    /**
     * 
     * @type {string}
     * @memberof NoteUpdate
     */
    content: string;
    /**
     * 
     * @type {number}
     * @memberof NoteUpdate
     */
    latitude: number;
    /**
     * 
     * @type {number}
     * @memberof NoteUpdate
     */
    longitude: number;
}

/**
 * Check if a given object implements the NoteUpdate interface.
 */
export function instanceOfNoteUpdate(value: object): value is NoteUpdate {
    if (!('content' in value) || value['content'] === undefined) return false;
    if (!('latitude' in value) || value['latitude'] === undefined) return false;
    if (!('longitude' in value) || value['longitude'] === undefined) return false;
    return true;
}

export function NoteUpdateFromJSON(json: any): NoteUpdate {
    return NoteUpdateFromJSONTyped(json, false);
}

export function NoteUpdateFromJSONTyped(json: any, ignoreDiscriminator: boolean): NoteUpdate {
    if (json == null) {
        return json;
    }
    return {
        
        'content': json['content'],
        'latitude': json['latitude'],
        'longitude': json['longitude'],
    };
}

export function NoteUpdateToJSON(value?: NoteUpdate | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'content': value['content'],
        'latitude': value['latitude'],
        'longitude': value['longitude'],
    };
}
