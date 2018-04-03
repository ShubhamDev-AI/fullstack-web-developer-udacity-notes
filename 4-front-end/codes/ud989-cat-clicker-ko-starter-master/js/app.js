var initialCats = [
    {
        clickCount: 0,
        name: 'Tabby',
        imgSrc: 'img/434164568_fea0ad4013_z.jpg',
        imgAttribution: 'https://www.flickr.com/photos/bigtallguy/434164568',
        nickNames: ['nick', 'messi', 'tom', 'el']
    },
    {
        clickCount: 0,
        name: 'Tiger',
        imgSrc: 'img/4154543904_6e2428c421_z.jpg',
        imgAttribution: 'https://www.flickr.com/photos/xshamx/4154543904',
        nickNames: ['tiger']
    },
    {
        clickCount: 0,
        name: 'Scaredy',
        imgSrc: 'img/22252709_010df3379e_z.jpg',
        imgAttribution: 'https://www.flickr.com/photos/kpjas/22252709',
        nickNames: ['aredy']
    },
    {
        clickCount: 0,
        name: 'Shadow',
        imgSrc: 'img/1413379559_412a540d29_z.jpg',
        imgAttribution: 'https://www.flickr.com/photos/malfet/1413379559',
        nickNames: ['light', 'dark', 'both']
    },
    {
        clickCount: 0,
        name: 'Sleepy',
        imgSrc: 'img/9648464288_2516b35537_z.jpg',
        imgAttribution: 'https://www.flickr.com/photos/onesharp/9648464288',
        nickNames: ['snorr']
    }
];

var Cat = function (data) {
    this.clickCount = ko.observable(data.clickCount);
    this.name = ko.observable(data.name);
    this.imgSrc = ko.observable(data.imgSrc);
    this.imgAttribution = ko.observable(data.imgAttribution);
    this.nickNames = ko.observableArray(data.nickNames);

    this.levelComputed = ko.computed(function () {
        if (this.clickCount() <= 10) {
            return "NewBorn";
        }

        if (this.clickCount() > 10 && this.clickCount() <= 20) {
            return "Toddle";
        }

        if (this.clickCount() > 20) {
            return "School";
        }

    }, this)

};


var ViewModel = function () {
    var self = this;

    this.catList = ko.observableArray([]);

    initialCats.forEach(function (catItem) {
        self.catList.push(new Cat(catItem));
    });

    this.currentCat = ko.observable(this.catList()[0]);

    this.increaseCounter = function () {
        self.currentCat().clickCount(self.currentCat().clickCount() + 1);
    };

    this.changeCurrentCat = function (cat) {
        self.currentCat(cat);
    };
};

ko.applyBindings(new ViewModel());