/* ============ Model ============ */

var model = {
    currentCat: 0,
    cats: [
        {counter: 0, name: 'tom', picture: 'cat_picture2.jpeg'},
        {counter: 0, name: 'jerry', picture: 'cat_picture1.jpg'},
        {counter: 0, name: 'mickey', picture: 'cat_picture3.jpeg'},
        {counter: 0, name: 'donald', picture: 'cat_picture4.jpeg'},
        {counter: 0, name: 'goofy', picture: 'cat_picture5.jpeg'}
    ]
};

/* ============ Controller ============ */

var controller = {

    init: function () {
        // set the display cat when first open web
        this.currentCat = model.cats[model.currentCat];

        // render initialize
        catView.init();
        catListView.init();
        adminView.init();
    },

    increaseCounter: function () {
        this.currentCat.counter += 1;
        catView.render();
        adminView.fillForm();
    },

    changeCurrentCat: function (catId) {
        this.currentCat = model.cats[catId];
        catView.render();
        adminView.fillForm();
    },

    getCurrentCat: function () {
        return this.currentCat;
    },

    getCats: function () {
        return model.cats;
    },

    showAdminFormView: function () {
        adminView.fillForm();
        adminView.enableForm();
    },

    disableAdminFormView: function () {
        adminView.disableForm();
    },

    saveAdminForm: function () {
        var data = adminView.getForm();
        var name = data.name;
        var img = data.img;
        var count = data.count;
        if (name && img && count){
            this.currentCat.name = name;
            this.currentCat.img = img;
            this.currentCat.count = count;
            catView.render();
            catListView.render();
            adminView.render();
        }
    }
};


/* ============ View ============ */
var catView = {

    init: function () {
        // get DOMs to manipulate
        this.$catName = $("#cat-name");
        this.$catImg = $("#cat-img");
        this.$catCount = $("#cat-count");

        // add event listener
        this.$catImg.on('click', function () {
            controller.increaseCounter();
        });

        // render view
        this.render();
    },

    render: function () {
        // get current cat to render
        var cat = controller.getCurrentCat();

        // change the DOMs
        this.$catName.text(cat.name);
        this.$catImg.attr("src", cat.picture);
        this.$catCount.text(cat.counter);
    }
};

var catListView = {

    init: function () {
        this.$catList = $("#cat-list");

        this.render();
    },

    render: function () {
        this.$catList.html('');
        var cats = controller.getCats();

        for (var i = 0; i < cats.length; i++) {
            var newItem = "<li id='cat-" + i + "'>" + cats[i].name + "</li>";
            this.$catList.append(newItem);
            $("#cat-"+i).on('click', function () {
                controller.changeCurrentCat(this.id.split("-")[1]);
            })
        }
    }
};

var adminView = {

    init: function () {
        this.$adminButton = $("#admin-button");
        this.$adminForm = $("#admin-form");
        this.$adminFormName = $("#admin-form-name");
        this.$adminFormImg = $("#admin-form-img");
        this.$adminFormCount = $("#admin-form-count");
        this.$adminFormCancel = $("#admin-form-cancel");
        this.$adminFormSave = $("#admin-form-save");

        this.$adminButton.on('click', function () {
            controller.showAdminFormView();
        });

        this.$adminFormCancel.on('click', function () {
            controller.disableAdminFormView();
        });

        this.$adminFormSave.on('click', function () {
            controller.saveAdminForm();
        });

        this.render();
    },

    render: function () {
        this.disableForm();
    },

    fillForm: function () {
        var cat = controller.getCurrentCat();
        this.$adminFormName.val(cat.name);
        this.$adminFormImg.val(cat.picture);
        this.$adminFormCount.val(cat.counter);
    },

    enableForm: function () {
        this.$adminForm.attr("style", "display: block");
    },

    disableForm: function () {
        this.$adminForm.attr("style", "display: none");
    },

    getForm: function () {
        return {
            'name': this.$adminFormName.val(),
            'img': this.$adminFormImg.val(),
            'count': this.$adminFormCount.val()
        }
    }

};


// Let controller do it
controller.init();