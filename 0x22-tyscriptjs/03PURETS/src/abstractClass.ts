class TakePhoto {
    constructor(
        public cameraMode: string,
        public filter: string,
        // public filter: number
    ){}

    abstract getSepia(): void
    getReelTime(): number{
        //complex calcuation
        return 8
    }
}


class Instagram extends TakePhoto {
    constructor(
        public cameraMode: string,
        public filter: String,
        public burst: number
        ) {
            super(cameraMode, filter)
        }

        getSepia(): void {
            console.log("Pepia")
        }
    
} ///inheritance

// const adikah = new TakePhoto("wide", "black")


export {}